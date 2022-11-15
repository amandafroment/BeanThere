function selectedButton(evt) {
  let evtVal = `${evt}val`;
  displayBtn = document.getElementById(evt);
  dataVal = document.getElementById(evtVal);
  if (dataVal.value === "false") {
    console.log(dataVal.value);
    displayBtn.style.backgroundColor = "#4e4235";
    dataVal.value = "true";
  } else {
    console.log(dataVal.value);
    displayBtn.style.backgroundColor = "#f4f4f4";
    dataVal.value = "false";
  }
}
