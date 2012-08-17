import sublime, sublime_plugin


# ########################################################
# ########################################################
# ########################################################
#   cfset - bad leading pound - <cfset[\s]*#
#   cfset - leading var pound - <cfset[^=\r\n]*=\s?#
#   cfset - pound signs inside cfset w/o quotes - match # in regex: <cfset[^>""]*>
# ########################################################
# ########################################################		
# ########################################################


class cfstatsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		a = self.view.find_all("<\!---[\s\S]*?--->")
		all = self.view.find_all("[\s\S]*")
		cfset_001 = self.view.find_all("<cfset[\s]*#")
		cfset_002 = self.view.find_all("<cfset[^=\r\n]*=\s?#")
		cfset_003 = self.view.find_all("<cfset[^>""]*>")

		self.view.add_regions("cfset_001",cfset_001,"source", sublime.HIDDEN)
		self.view.add_regions("cfset_002",cfset_002,"source", sublime.HIDDEN)
		self.view.add_regions("cfset_003",cfset_003,"source", sublime.HIDDEN)

		self.view.add_regions("Highlight", a, "source", sublime.HIDDEN)
		self.view.add_regions("AllContent", all, "source", sublime.HIDDEN)
		b = self.view.get_regions("Highlight")
		g = self.view.get_regions("AllContent")
		c = 0
		print ""
		print "CF Stats and Standards"
		print "---------------------------------"
		print ">> General Stats:"
		for allregion in g:
			h = len(self.view.substr(allregion))
		for region in b:
			c += len(self.view.substr(region))
		if c > 1024:			
			print "Comment size is ~"+str((c/1024))+"Kb ("+str(c)+" bytes) out of a total file size of ~"+str(h/1024)+"Kb ("+str(c*100/h)+"%)"
		else:
			print "Comment size is ~"+str(c)+" bytes out of a total file size of ~"+str(h/1024)+"Kb ("+str(c*100/h)+"%)"		
		print ""
		print ">> Possible Coding Standards Violations: "
		h = self.view.get_regions("cfset_001")
		for region in h:
			(row, col) = self.view.rowcol(region.begin())
			print "Line: "+str(row+1)+ " - Issue: Hashes are not necessary unless variable/method resides between quotes - "+self.view.substr(self.view.line(region))
		h = self.view.get_regions("cfset_002")
		for region in h:
			(row, col) = self.view.rowcol(region.begin())
			print "Line: "+str(row+1)+ " - Issue: Hashes are not necessary unless variable/method resides between quotes - "+self.view.substr(self.view.line(region))
			
		