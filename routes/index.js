const express = require('express')
const router = express.Router()


router.get('/', (req, res) => {
  const env = {
      navLogo: process.env.NAV_LOGO,
      facebook: process.env.FACEBOOK,
      instagram: process.env.INSTAGRAM,
      name: process.env.NAME,
      address: process.env.ADDRESS,
      phone: process.env.PHONE,
      hours_early: process.env.HOURS_EARLY,
      hours_late: process.env.HOURS_LATE,
      closed: process.env.CLOSED
  }

  const data = {
    greeting: 'Welcome to my Restaurant',
    description: 'Great place'
  }

  res.render('index', data)
})


router.get('/mas',(req,res, next) =>{
  const data ={
      title: "Joe's Coffee"
  }
  res.render('+',data)

})

router.get('/homecafeteria',(req,res, next) =>{
  const data ={
      title: "Joe's Coffee"
  }
  res.render('homecafeteria',data)

})

module.exports = router