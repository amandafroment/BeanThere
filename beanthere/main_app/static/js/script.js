function selectedButton(evt) {
    console.log(evt)
  let evtVal = `${evt}val`;
      console.log(evtVal)
  displayBtn = document.getElementById(evt);
  dataVal = document.getElementById(evtVal);
  if (dataVal.value === "false") {
    console.log(dataVal.value);
    displayBtn.style.backgroundColor = "#4e4235";
    displayBtn.style.color = "#F7F7F7";
    dataVal.value = "true";
  } else {
    console.log(dataVal.value);
    displayBtn.style.backgroundColor = "#f4f4f4";
    dataVal.value = "false";
  }
}
