const express = require('express');
const session = require('express-session');

const app = express();
const port = 3000;

app.set('view engine', 'ejs'); // Set EJS as the view engine

app.use(session({
    secret: 'super_secret_key',
    resave: false,
    saveUninitialized: true
}));

app.get('/', (req, res) => {
    // Increment the visit count in the session
    req.session.visit_count = (req.session.visit_count || 0) + 1;

    res.render('index_session', { visit_count: req.session.visit_count });
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
