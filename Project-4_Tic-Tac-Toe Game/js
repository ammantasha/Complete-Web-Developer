var symbol = "X";
var display = document.getElementById("player");
var data;

function printx(number){
    var data = document.getElementById("row" + number);
    console.log(data);
  
    if(data.innerText == ""){
        data.innerText = symbol;
        winner();
        checkSymbol();
        display.innerHTML = "<span> Now " + symbol + " Turn </span>";
    }
}

function checkSymbol(){
    if(symbol == "X")
        symbol = "O";
    else
        symbol = "X"; 
}

function getBox(no){
    return document.getElementById("row" + no).innerHTML;
}

function checkMove(a,b,c,m){
    if(getBox(a) == m && getBox(b) == m && getBox(c) == m)
        return true;
    else
        return false;   
}

function winner(){
    if(checkMove(1,2,3,symbol) || checkMove(4,5,6,symbol) || checkMove(7,8,9,symbol)
        || checkMove(1,4,7,symbol) || checkMove(2,5,8,symbol) || checkMove(3,6,9,symbol)
        || checkMove(1,5,9,symbol) || checkMove(7,5,3,symbol)){
           
            display.innerHTML = "<span id='win'>Congratulations!!! " + symbol + " WON!!! </span>";
            for(var i=1; i<=9; i++){
                document.getElementById("row" + i).innerHTML = "";
            }
            throw "game end";
    }
    else{
        if(getBox(1) != "" && getBox(2) != "" && getBox(3) != "" &&
            getBox(4) != "" && getBox(5) != "" && getBox(6) != "" &&
            getBox(7) != "" && getBox(8) != "" && getBox(9) != ""){

                display.innerHTML = "OOps!!! It's a Tie...Play again";
        
                for(var i=1; i<=9; i++){
                    document.getElementById("row" + i).innerHTML = "";
                }
                throw "game end";
        }
    }
}
