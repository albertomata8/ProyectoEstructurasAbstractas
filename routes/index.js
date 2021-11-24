// Full Documentation - https://docs.turbo360.co
const express = require('express')
const router = express.Router()


router.get('/', (req, res) => {
  const data = {
    cdn:process.env.TURBO_CDN,
    greeting: 'Welcome to my Restaurant',
    description: 'Great place'
  }

  res.render('index', data)
})



module.exports = router
