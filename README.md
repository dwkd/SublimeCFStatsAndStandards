SublimeCFStatsAndStandards
==========================
The idea is to get a few useful stats about a cfm/cfc file and warn user of possible bad code practices.

<b>Results contains the following stats:</b><br />
<ul>
	<li>filename</li>
	<li>filesize</li>
	<li>comment size in kb and %</li>
	<li>javascript stat: number of external javascript files loaded</li>
	<li>javascript stat: total size of all In-file javascript</li>
	<li>css stat: total size of in-file css declarations</li>
	<li>css stat: total size of in-line css (unlooped)</li>
	<li>cfml stat: tag vs script usage in %</li>
	<li>cfml stat: number of cfdumps/writeDumps</li>
	<li>cfml stat: number of cfaborts/aborts/aborts()</li>
	<li>number of cfdumps and writeDumps and at what line numbers</li>
</ul>

<b>Standards searched for:</b><br />
<ul>
	<li>cfqueryparam missing that could cause security hole</li>
	<li>cfset unnecessary hash signs outside quotes</li>
	<li>cfset unnecessary dummy variables used to perform operations that directly affect the data such as having &lt;cfset tempvar = ArrayAppend(myarray,"myvalue")&gt; unless the boolean return is useful</li>
	<li>cfset modifying application, server or session shared variables outside of an exclusive cflock</li>	
	<li>proper indentation</li>
	<li>in-file css declarations should be consolidated to .css file(s)</li>
	<li>in-file js function declarations should be consolidated to .js file(s)</li>
</ul>

Work in progress. <br />
More standards to come. <br />
If you'd like to see another stat or standard, shoot me an email at webmaster@thebluepipe.com<br />

Installing
============
1. Download the project from github. (Press the Download Zip button.)
2. Open the downloaded zip file.
3. Select and copy the folder dwkd-SublimeCFStatsAndStandards....
4. Open Sublime Text Editor
5. Under the Preferences menu, press Browse Packages....
6. Paste the folder dwkd-SublimeCFStatsAndStandards... to the Packages directory.
7. Restart Sublime

How-to
======
Open file to be inspected and press:<br />
CTRL+ALT+S (Windows & Linux)<br />
COMMAND+ALT+S (Mac OS)

License
=======
Copyright 2012 Alex Trican. All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY Alex Trican "AS IS" AND ANY EXPRESS OR IMPLIED
WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
EVENT SHALL Alex Trican OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
