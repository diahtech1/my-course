function birthYear(name:string, year:number): string {
    // check if user input name
    const defaultyear: number = 2026
    if (!name) {
        return("enter your name")
        
    } 
    // check if user birthyear is valid
    if (year > defaultyear) {
       return ("birth year cannot be greater than 2026")
        
    }
    // send greeting message  
    let userAge:number = (defaultyear - year)
    return `Welcome! ${name}. You are ${userAge} years old`;
    

}

const result: string = birthYear("Josiah", 2023)
console.log(result)
