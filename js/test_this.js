'use strict'
const obj = {
    test: function(){
      (function(){
        console.log(this);
      })(); //немедленно вызываемая функция внутри другой функции
    }
  }

  obj.test(); // мне говорят, что в консоль выведется obj. это неправда
  debugger