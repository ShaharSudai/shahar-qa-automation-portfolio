@echo off
title Bug Tracker API - Newman Report Generator
color 0A

echo ======================================================
echo     Running Newman Tests for Bug Tracker API Project
echo ======================================================
echo.

if not exist "Reports" mkdir Reports

newman run "postman\Bug Tracking API Tests.postman_collection.json" ^
  -e "postman\Bug Tracker.postman_environment.json" ^
  -r htmlextra ^
  --delay-request 1000 ^
  --reporter-htmlextra-export "Reports\BugTracker_API_Report.html" ^
  --reporter-htmlextra-title "Bug Tracker API - Automation Report"

echo.
echo ======================================================
echo   ✅ Newman run complete!
echo   📄 Report generated at: Reports\BugTracker_API_Report.html
echo ======================================================
echo.

start "" "Reports\BugTracker_API_Report.html"

pause
