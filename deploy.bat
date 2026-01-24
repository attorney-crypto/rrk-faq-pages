@echo off
set RAILWAY_TOKEN=c5206d1b-e582-422a-a0dc-19eb07e35288
cd /d "%~dp0"
echo Deploying to Railway...
railway up --service rrk-law-faq
pause
