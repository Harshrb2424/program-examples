const express = require('express');
const cookieParser = require('cookie-parser');
const path = require('path');

const app = express();
const port = 3000;

app.use(cookieParser());
app.set('view engine', 'ejs');

// Middleware to pass the userLanguage to all routes
app.use((req, res, next) => {
  res.locals.userLanguage = req.cookies.user_language;
  next();
});

// Routes
app.get('/', (req, res) => {
  res.render('index');
});

app.get('/set_language/:language', (req, res) => {
  const language = req.params.language;

  // Set the language preference in a cookie
  res.cookie('user_language', language);
  res.render('set_language');
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
