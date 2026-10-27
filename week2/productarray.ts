const Products:{ name:string; price:number} []= [
    {name: "iphone 7plus", price: 20},
    {name: "iphone 8plus", price: 30},
    {name: "XR", price: 40},
    {name: "11-pro-Max", price: 50},
    {name: "12-pro-Max", price: 60},
    {name: "13-pro-Max", price: 70},
    {name: "14-pro-Max", price: 80},
    {name: "15-pro-Max", price: 90}

]

const belowfifty = Products.filter(product => product.price <= 50)
console.log(belowfifty)