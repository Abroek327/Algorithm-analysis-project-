const puppeteer = require('puppeteer');
const stealth = require('puppeteer-extra-plugin-stealth');

//Sets commonly used default values to help webscraper blend in with regular traffic
const options = {
    headless: false,
    ignoreHTTPSErrors: true,
    args: [
        "--no-sandbox",
        "--disable-setuid-sandbox",
        "--ignore-certificate-errors",
        "--lang=en-US,en;q=0.9",
        "--disable-dev-shm-usage",
    ],
    defaultViewport: {width: 1366, height:768},
}

//Launch Puppeteer
puppeteer.launch({headless: false}).then(async browser =>{

    const page = await browser.newPage();

    //Waiting on networkl Idle2 event allows the page to fully load
    await page.goto('https://www.google.com', {waitUntil: 'networkidle2'});

    await browser.close();
});