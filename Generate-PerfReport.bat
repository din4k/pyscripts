@ECHO OFF
set filename=User-PC_%date:~4,2%%date:~7,2%%date:~10,4%
set scrhome="C:\Program Files (x86)\Hitachi"
set outfile="C:\Program Files (x86)\Hitachi\jp1pcWebCon\Reports\User-PC\%filename%_CPU_test"
set configfile="C:\Program Files (x86)\Hitachi\jp1pcWebCon\Reports\jpcrpt-parameters-CPU-report.xml"
set c=%outfile:~1,-1%
set d="%c%.txt"

REM -- "C:\Program Files (x86)\Hitachi\jp1pcWebCon\tools\jpcrpt.exe" -o %outfile% -dateformat "pattern-MMddyyyy" -agent TA1User-PC %configfile%
"C:\Program Files (x86)\Hitachi\jp1pcWebCon\tools\jpcrpt.exe" -o %outfile% -agent TA1User-PC %configfile%
REM -- IF %ERRORLEVEL% NEQ 0 GOTO :ERROR
REM -- converting the pfm file to csv format

rem move %outfile% %d%
copy %outfile% %d%
REM -- removing the top 5 script header lines in the report
set tempfile="%c%_temp.txt"
echo %tempfile%
more /E +5 %d% > %tempfile%
REM -- :EOF
REM -- msg * "%d%" Report generated successfully!
REM -- exit

REM -- :ERROR
REM -- msg * "%d%" Failed to generated report. Please investigate.
REM -- powershell -ExecutionPolicy ByPass -command "New-EventLog -LogName Application -Source PerfReport; write-eventlog -logname Application -source PerfReport -EntryType ERROR -Message 'Failed to generated report. Please investigate.' -EventId 10201"
REM -- exit

