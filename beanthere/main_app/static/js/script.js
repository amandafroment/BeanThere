    console.log("script")

    let choice = document.querySelector("#select4");

    document.getElementById("#select4");
    document.getElementById("#select5");
    document.getElementById("#select6");
    document.getElementById("#select7");
    document.getElementById("#select8");
    document.getElementById("#select9");
    document.getElementById("#select10");

    // choice.addEventListener("click", selectedButton);
    // let collection = [];

    function selectedButton(evt) {
        console.log("working")
        console.log(evt.target)
        document.getElementById("select4").style.backgroundColor = "#988C7A";
    }