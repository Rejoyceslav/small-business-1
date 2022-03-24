// JQuery //

// Sidebar accordion menu

$(document).ready(function() {

    $("#accordian h3").click(function() {
        $("#accordian ul ul").slideUp();

        if(!$(this).next().is(":visible")) {
        $(this).next().slideDown();
        }
    });

});

// When the user scrolls down 100px from the top:
// - resize the navbar
// - the logo size and trim the subtitle
//- fade away hero text and hero button

window.onscroll = function() {
    navbarTransitionFunction(),
    hideHeroTextFunction(),
    hideHeroButtonFunction()
};

function navbarTransitionFunction() {
  if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
    document.getElementById("navbar-logo").style.clipPath = "inset(0px 0px 11.5% 0px)";
    document.getElementById("navbar-logo").style.height = "6.0vh";
    document.getElementById("navbar-logo").style.margin = "0px 0px -15px 0px";
    document.getElementById("navbar-logo").style.transitionDuration = "0.720s";
    document.getElementById("navbar").classList.add("navbar-scrolled");
    document.getElementById("navbar-divider-left").style.width = "120px";
    document.getElementById("navbar-divider-left").style.transitionDuration = "0.720s";
  } else {
    document.getElementById("navbar-logo").style.clipPath = "inset(0px 0px 0px 0px)";
    document.getElementById("navbar-logo").style.height = "10.5vh";
    document.getElementById("navbar-logo").style.margin = "0px 0px 0px 0px";
    document.getElementById("navbar").classList.remove("navbar-scrolled");
    document.getElementById("navbar-divider-left").style.width = "";
    document.getElementById("navbar-divider-middle").style.width = "";
  }
}

function hideHeroTextFunction() {
  if (document.body.scrollTop > 380 || document.documentElement.scrollTop > 380) {
    document.getElementById("hero-text").style.transitionDuration = "0.6s";
    document.getElementById("hero-content-bg").style.transitionDuration = "0.6s";
    document.getElementById("hero-text").style.color = "transparent";
    document.getElementById("hero-text").style.backgroundColor = "transparent";
    document.getElementById("hero-text").style.textShadow = "2px 2px rgba(24,26,27,0.0)";
    document.getElementById("hero-content-bg").style.backgroundColor = "transparent";
  } else {
    document.getElementById("hero-text").style.color = "";
    document.getElementById("hero-text").style.textShadow = "2px 2px rgba(24,26,27,0.55)";
    document.getElementById("hero-content-bg").style.backgroundColor = "";
    document.getElementById("hero-text").style.backgroundColor = "";
  }
}

function hideHeroButtonFunction() {
  if (document.body.scrollTop > 490 || document.documentElement.scrollTop > 490) {

    document.getElementById("hero-button").style.backgroundColor = "transparent";
    document.getElementById("hero-button").style.color = "transparent";
    document.getElementById("hero-button").style.border = "none";
  } else {
    document.getElementById("hero-button").style.backgroundColor = "";
    document.getElementById("hero-button").style.color = "white";
    document.getElementById("hero-button").style.border = "";
  }
}




//const linkOfertaLink = document.getElementById("oferta-link");
//linkOfertaLink.onclick = ScrollToOffer;
//
//function ScrollToOffer() {
//  const scrollToOferta = document.getElementById("oferta-box");
//  scrollToOferta.scrollIntoView({behavior: "smooth", block: "center"});
//}
//
//const linkONasLink = document.getElementById("onas-link");
//linkONasLink.onclick = ScrollToAbout;
//
//function ScrollToAbout() {
//  const scrollToONas = document.getElementById("onas-box");
//  scrollToONas.scrollIntoView({behavior: "smooth", block: "center"});
//}



// Scrolling for basic float menu
// to text and mark text, unmark previous text:
//const LinkOleje = document.getElementById("oleje_link");
//LinkOleje.onclick = menulink2;
//function menulink2() {
//    elements = document.getElementsByClassName("item-title");
//    for (var i = 0; i < elements.length; i++) {
//        elements[i].classList.remove("item-title-highlight");
//    }
//    document.getElementById("oleje_title").classList.add("item-title-highlight")
//    const box = document.getElementById("oleje")
//    box.scrollIntoView({behavior: "smooth", block: "center"});
//}
//
//const LinkLozyska = document.getElementById("lozyska_link");
//LinkLozyska.onclick = menulink1;
//function menulink1() {
//    elements = document.getElementsByClassName("item-title");
//    for (var i = 0; i < elements.length; i++) {
//        elements[i].classList.remove("item-title-highlight");
//    }
//    document.getElementById("lozyska_title").classList.add("item-title-highlight")
//    const box = document.getElementById("lozyska")
//    box.scrollIntoView({behavior: "smooth", block: "center"});
//}
//
//const LinkPrzepustnice = document.getElementById("przepustnice_link");
//LinkPrzepustnice.onclick = menulink3;
//function menulink3() {
//    elements = document.getElementsByClassName("item-title");
//    for (var i = 0; i < elements.length; i++) {
//        elements[i].classList.remove("item-title-highlight");
//    }
//    document.getElementById("przepustnice_title").classList.add("item-title-highlight")
//    const box = document.getElementById("przepustnice")
//    box.scrollIntoView({behavior: "smooth", block: "center"});
//}
//
//const LinkWzierniki = document.getElementById("wzierniki_link");
//LinkWzierniki.onclick = menulink4;
//function menulink4() {
//    elements = document.getElementsByClassName("item-title");
//    for (var i = 0; i < elements.length; i++) {
//        elements[i].classList.remove("item-title-highlight");
//    }
//    document.getElementById("wzierniki_title").classList.add("item-title-highlight")
//    const box = document.getElementById("wzierniki")
//    box.scrollIntoView({behavior: "smooth", block: "center"});
//}
//
//const LinkFiltry = document.getElementById("filtry_link");
//LinkFiltry.onclick = menulink5;
//function menulink5() {
//    elements = document.getElementsByClassName("item-title");
//    for (var i = 0; i < elements.length; i++) {
//        elements[i].classList.remove("item-title-highlight");
//    }
//    document.getElementById("filtry_title").classList.add("item-title-highlight")
//    const box = document.getElementById("filtry")
//    box.scrollIntoView({behavior: "smooth", block: "center"});
//}
//
//const LinkManometry = document.getElementById("manometry_link");
//LinkManometry.onclick = menulink6;
//function menulink6() {
//    elements = document.getElementsByClassName("item-title");
//    for (var i = 0; i < elements.length; i++) {
//        elements[i].classList.remove("item-title-highlight");
//    }
//    document.getElementById("manometry_title").classList.add("item-title-highlight")
//    const box = document.getElementById("manometry")
//    box.scrollIntoView({behavior: "smooth", block: "center"});
//}
//
//const LinkPasyNapedowe = document.getElementById("pasy_napedowe_link");
//LinkPasyNapedowe.onclick = menulink7;
//function menulink7() {
//    elements = document.getElementsByClassName("item-title");
//    for (var i = 0; i < elements.length; i++) {
//        elements[i].classList.remove("item-title-highlight");
//    }
//    document.getElementById("pasy_napedowe_title").classList.add("item-title-highlight")
//    const box = document.getElementById("pasy_napedowe")
//    box.scrollIntoView({behavior: "smooth", block: "center"});
//}
//
//const LinkPrzylacza = document.getElementById("przylacza_link");
//LinkPrzylacza.onclick = menulink8;
//function menulink8() {
//    elements = document.getElementsByClassName("item-title");
//    for (var i = 0; i < elements.length; i++) {
//        elements[i].classList.remove("item-title-highlight");
//    }
//    document.getElementById("przylacza_title").classList.add("item-title-highlight")
//    const box = document.getElementById("przylacza")
//    box.scrollIntoView({behavior: "smooth", block: "center"});
//}


//Scrolling for sidebar
const LinkOleje = document.getElementById("oleje_link");
LinkOleje.onclick = menulink2;
function menulink2() {
    elements = document.getElementsByClassName("item-title");
    for (var i = 0; i < elements.length; i++) {
        elements[i].classList.remove("item-title-highlight");
    }
    document.getElementById("oleje_title").classList.add("item-title-highlight")
    const box = document.getElementById("oleje")
    box.scrollIntoView({behavior: "smooth", block: "center"});
}

const LinkLozyska = document.getElementById("lozyska_link");
LinkLozyska.onclick = menulink1;
function menulink1() {
    elements = document.getElementsByClassName("item-title");
    for (var i = 0; i < elements.length; i++) {
        elements[i].classList.remove("item-title-highlight");
    }
    document.getElementById("lozyska_title").classList.add("item-title-highlight")
    const box = document.getElementById("lozyska")
    box.scrollIntoView({behavior: "smooth", block: "center"});
}

const LinkPrzepustnice = document.getElementById("przepustnice_link");
LinkPrzepustnice.onclick = menulink3;
function menulink3() {
    elements = document.getElementsByClassName("item-title");
    for (var i = 0; i < elements.length; i++) {
        elements[i].classList.remove("item-title-highlight");
    }
    document.getElementById("przepustnice_title").classList.add("item-title-highlight")
    const box = document.getElementById("przepustnice")
    box.scrollIntoView({behavior: "smooth", block: "center"});
}

const LinkWzierniki = document.getElementById("wzierniki_link");
LinkWzierniki.onclick = menulink4;
function menulink4() {
    elements = document.getElementsByClassName("item-title");
    for (var i = 0; i < elements.length; i++) {
        elements[i].classList.remove("item-title-highlight");
    }
    document.getElementById("wzierniki_title").classList.add("item-title-highlight")
    const box = document.getElementById("wzierniki")
    box.scrollIntoView({behavior: "smooth", block: "center"});
}

const LinkFiltry = document.getElementById("filtry_link");
LinkFiltry.onclick = menulink5;
function menulink5() {
    elements = document.getElementsByClassName("item-title");
    for (var i = 0; i < elements.length; i++) {
        elements[i].classList.remove("item-title-highlight");
    }
    document.getElementById("filtry_title").classList.add("item-title-highlight")
    const box = document.getElementById("filtry")
    box.scrollIntoView({behavior: "smooth", block: "center"});
}

const LinkManometry = document.getElementById("manometry_link");
LinkManometry.onclick = menulink6;
function menulink6() {
    elements = document.getElementsByClassName("item-title");
    for (var i = 0; i < elements.length; i++) {
        elements[i].classList.remove("item-title-highlight");
    }
    document.getElementById("manometry_title").classList.add("item-title-highlight")
    const box = document.getElementById("manometry")
    box.scrollIntoView({behavior: "smooth", block: "center"});
}

const LinkPasyNapedowe = document.getElementById("pasy_napedowe_link");
LinkPasyNapedowe.onclick = menulink7;
function menulink7() {
    elements = document.getElementsByClassName("item-title");
    for (var i = 0; i < elements.length; i++) {
        elements[i].classList.remove("item-title-highlight");
    }
    document.getElementById("pasy_napedowe_title").classList.add("item-title-highlight")
    const box = document.getElementById("pasy_napedowe")
    box.scrollIntoView({behavior: "smooth", block: "center"});
}

const LinkPrzylacza = document.getElementById("przylacza_link");
LinkPrzylacza.onclick = menulink8;
function menulink8() {
    elements = document.getElementsByClassName("item-title");
    for (var i = 0; i < elements.length; i++) {
        elements[i].classList.remove("item-title-highlight");
    }
    document.getElementById("przylacza_title").classList.add("item-title-highlight")
    const box = document.getElementById("przylacza")
    box.scrollIntoView({behavior: "smooth", block: "center"});
}

//Sticksy.js.org menu
var stickyEl = new Sticksy('.js-sticky-widget', {topSpacing: 70})
// you can handle state changing
stickyEl.onStateChanged = function (state) {
    if(state === 'fixed') {
        stickyEl.nodeRef.classList.add('widget--sticky')
    } else {
        stickyEl.nodeRef.classList.remove('widget--sticky')
    }
}
