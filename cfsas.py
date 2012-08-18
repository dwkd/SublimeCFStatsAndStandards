import sublime, sublime_plugin
import math

# 
#   cfscript - match only cfscript - <cfscript>[\s\S]*?<\/cfscript>
#   cfml - match all cf tags except cfscript <\/?cf(?!script)[^>]*># 
# 
#   cfset - leading hash - <cfset[\s]*#
#   cfset - post equal leading hash - <cfset[^=\r\n]*=\s?#
#   cfset - hash in a quote-free cfset - match # in <cfset[^>\"\r\n]*>
# 
# 
# 

class cfsasCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		#end output message
		f = self.view
		returnMessage = "\nCF Stats and Standards \n\nFile: "+str(f.file_name())+"\nSize: ~"+str(f.size()/1024)+"Kb ("+str(f.size())+" bytes)\n\n General Stats:\n =========================================================================================================\n"
		
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
			m = " -Comment size is ~"+str((c/1024))+"Kb ("+str(c)+" bytes) out of a total file size of ~"+str(h/1024)+"Kb ("+str(c*100/h)+"%)\n"
			returnMessage += m
		elif c == 0:
			returnMessage += " -Comment size is 0 bytes out of a total file size of ~"+str(h/1024)+"Kb (0%)\n"
		else:
			m = " -Comment size is ~"+str(c)+" bytes out of a total file size of ~"+str(h/1024)+"Kb ("+str(c*100/h)+"%)\n"
			returnMessage += m

		#cf code: tag vs script usage
		cfcode_cftags = self.view.find_all("<\/?cf(?!script)[^>]*>")
		cfcode_cfscript = self.view.find_all("<cfscript>[\s\S]*?<\/cfscript>")

		self.view.add_regions("cfcode_cftags",cfcode_cftags,"source",sublime.HIDDEN)
		self.view.add_regions("cfcode_cfscript",cfcode_cfscript,"source",sublime.HIDDEN)

		h = self.view.get_regions("cfcode_cftags")
		c = 0
		for region in h:
			c += len(self.view.lines(region))
		
		h = self.view.get_regions("cfcode_cfscript")
		d = 0
		for region in h:
			d += len(self.view.lines(region))
		
		returnMessage += " -CFML: Tag vs Script usage\n   %.2f" % (c*100/float(c+d)) +"% tags\n   "+"%.2f" % (d*100/float(c+d)) +"% script\n"

		#cfset validation
		cfset_001 = self.view.find_all("<cfset[\s]*#")
		cfset_002 = self.view.find_all("<cfset[^=\r\n]*=\s?#")
		cfset_003 = self.view.find_all("<cfset[^>\"\r\n]*>")

		self.view.add_regions("cfset_001",cfset_001,"source", sublime.HIDDEN)
		self.view.add_regions("cfset_002",cfset_002,"source", sublime.HIDDEN)
		self.view.add_regions("cfset_003",cfset_003,"source", sublime.HIDDEN)
				
		returnMessage += "\n\n Possible Coding Standards Violations: \n =========================================================================================================\n"
		h = self.view.get_regions("cfset_001")
		for region in h:
			(row, col) = self.view.rowcol(region.begin())
			m = " -Line: "+str(row+1)+ " - Issue: Hashes are not necessary unless variable/method resides between quotes - "+self.view.substr(self.view.line(region))+"\n"
			returnMessage += m
		h = self.view.get_regions("cfset_002")
		for region in h:
			(row, col) = self.view.rowcol(region.begin())
			m = " -Line: "+str(row+1)+ " - Issue: Hashes are not necessary unless variable/method resides between quotes - "+self.view.substr(self.view.line(region))+"\n"
			returnMessage += m
		h = self.view.get_regions("cfset_003")
		for region in h:
			a = self.view.substr(region).find("#")
			if a != -1:
				(row, col) = self.view.rowcol(region.begin())
				m = " -Line: "+str(row+1)+ " - Issue: Hashes are not necessary unless variable/method resides between quotes - "+self.view.substr(self.view.line(region))+"\n"
				returnMessage += m

		#send to new file
		w = self.view.window()
		w.run_command("new_file")
		v = w.active_view()
		v.insert(edit,0,returnMessage)

		