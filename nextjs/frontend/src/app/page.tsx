import React, {  } from 'react'

export default function Home(this: any) {
  //rows currently set to filler data
  let rows = [0,1,2,3];
  function setRows(){
    //initialize rows with an API call
  }
  //customer list: ID, name, address, zipcode, phone, city, country, notes
  //customer: ID, storeID, first, last, email, addressID, active, date
  
  

    return(
      <table id="simple-board">
       <tbody>
         {rows}
       </tbody>
      </table>
    )

}
