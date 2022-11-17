    console.log("script")

    let choice = document.querySelector("#select4");
    choice.addEventListener("click", selectedButton);
    choice.onclick = function() {
        console.log("work")
    }
    // let collection = [];

    function selectedButton(evt) {
        console.log("working")
        console.log(evt.target.attr("id"))
        document.getElementsById().style.backgroundColor = "#988C7A";
    }