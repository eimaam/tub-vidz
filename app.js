// navigation togglers defined
const showNav = document.getElementById('showNav')
const hideNav = document.getElementById('hideNav')

// mobile menu set to variable mNav
const mNav = document.getElementById('mNav')

// function to handle toggling event
function navToggler(){
    if(mNav.style.display != "flex"){
        mNav.style.display = "flex"
        showNav.style.display = 'none'
        hideNav.style.display = 'block'
    }else{
        mNav.style.display = 'none'
        showNav.style.display = 'block'
        hideNav.style.display = 'none'
    }
}

// function to call on mobile navigation display function above
const showHideNav = () => {
    showNav.addEventListener("click", navToggler())

}