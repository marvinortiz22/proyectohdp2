document.getElementById("id_user").onchange=function(){
               
    var user = document.getElementById("id_user");
    var select = document.getElementById("select");
    select.innerHTML = "";
    if(user.value == "1"){
        var optionArray = ["|","camaro|Camaro","corvette|Corvette","impala|Impala"];
    } else if(user.value == "Dodge"){
        var optionArray = ["|","avenger|Avenger","challenger|Challenger","charger|Charger"];
    } else if(user.value == "Ford"){
        var optionArray = ["|","mustang|Mustang","shelby|Shelby"];
    }
    for(var option in optionArray){
        var pair = optionArray[option].split("|");
        var newOption = document.createElement("option");
        newOption.value = pair[0];
        newOption.innerHTML = pair[1];
        select.options.add(newOption);
    }
}