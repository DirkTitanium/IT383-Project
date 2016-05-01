var config = {
    lang: 'nl',
    time: {
        timeFormat: 12
    },
    weather: {
        //change weather params here:
        //units: metric or imperial
        params: {
            q: 'West Point, NY',
            units: 'imperial',
            // if you want a different lang for the weather that what is set above, change it here
            lang: 'nl',
            APPID: '83bb986b86b2e3294567cd5c1cd4c46e'
        }
    },
    compliments: {
        interval: 30000,
        fadeInterval: 4000,
        morning: [
            '',
            '',
            ''
        ],
        afternoon: [
            
            '',
            
        ],
        evening: [
            
            
            ''
        ]
    },
    calendar: {
        maximumEntries: 10,
        url: "https://p01-calendarws.icloud.com/ca/subscribe/1/n6x7Farxpt7m9S8bHg1TGArSj7J6kanm_2KEoJPL5YIAk3y70FpRo4GyWwO-6QfHSY5mXtHcRGVxYZUf7U3HPDOTG5x0qYnno1Zr_VuKH2M"
    },
    news: {
        feed: 'http://www.nytimes.com/services/xml/rss/nyt/HomePage.xml'
    }
}
