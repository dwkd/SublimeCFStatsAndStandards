import sublime, sublime_plugin


# <!---########################################################
# ########################################################
# ########################################################
#   cfset - bad leading pound - <cfset[\s]*#
#   cfset - leading var pound - <cfset[^=\r\n]*=\s?#
#   cfset - pound signs inside cfset w/o quotes - match # in regex: <cfset[^>""]*>
# ########################################################
# ########################################################		
# ########################################################--->


class cfstatsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		#end output message
		returnMessage = "\nCF Stats and Standards \n General Stats:\n"
		
		all = self.view.find_all("[\s\S]*")
		self.view.add_regions("AllContent", all, "source", sublime.HIDDEN)
		g = self.view.get_regions("AllContent")
		for allregion in g:
			h = len(self.view.substr(allregion))

		#comments
		cf_comment_01 = self.view.find_all("<\!---[\s\S]*?--->")
		cf_comment_02 = self.view.find_all("\/\*[\s\S]*?\*\/")

				
		self.view.add_regions("cf_comment_01", cf_comment_01, "source", sublime.HIDDEN)
		self.view.add_regions("cf_comment_02", cf_comment_02, "source", sublime.HIDDEN)

		c = 0
		c1 = self.view.get_regions("cf_comment_01")
		c2 = self.view.get_regions("cf_comment_02")

		for region in c1:
			c += len(self.view.substr(region))
		for region in c2:
			c += len(self.view.substr(region))
		if c > 1024:			
			returnMessage += " -Comment size is ~"+str((c/1024))+"Kb ("+str(c)+" bytes) out of a total file size of ~"+str(h/1024)+"Kb ("+str(c*100/h)+"%)\n"
		else:
			returnMessage += " -Comment size is ~"+str(c)+" bytes out of a total file size of ~"+str(h/1024)+"Kb ("+str(c*100/h)+"%)\n"


		print returnMessage

		

		cfset_001 = self.view.find_all("<cfset[\s]*#")
		cfset_002 = self.view.find_all("<cfset[^=\r\n]*=\s?#")
		cfset_003 = self.view.find_all("<cfset[^>""]*>")

		self.view.add_regions("cfset_001",cfset_001,"source", sublime.HIDDEN)
		self.view.add_regions("cfset_002",cfset_002,"source", sublime.HIDDEN)
		self.view.add_regions("cfset_003",cfset_003,"source", sublime.HIDDEN)
				
		
		
				
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
			
		