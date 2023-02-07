class Amazing {
    static cool() {
      console.log('cool');
    }
    wow(){
      console.log('wow');
    }
  }

  class Wonderful extends Amazing {
    static awesome() {
        super.cool();
        console.log('awesome')
    }
    great() {
        Amazing.cool();
    }
  }

  Amazing.cool();
  let am_1 = new Amazing()
  am_1.wow()
  Wonderful.cool();
  Wonderful.awesome();

  const instance = new Wonderful();

  instance.great();
  debugger