const catelog = require("./catelog.json")
const nav=require("./nav.json")
module.exports = {
    title: '启蒙文本网',
    description: '毛选+金庸',
    themeConfig: {
        nextLinks: true,
        prevLinks: true,
        sidebar: catelog,
        displayAllHeaders: false,
        nav: nav,
    }
}