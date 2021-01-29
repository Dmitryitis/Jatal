$(function () {

    //Preloader
    var body = $('body');
    $(window).on('load', function () {
        body.addClass('loaded_hiding');

        window.setTimeout(function () {
            body.addClass('loaded');
            body.removeClass('loaded_hiding');
        }, 1500);
    });

    //Burger
    // $("#burger").on("click", function (event) {
    //     event.preventDefault();
    //
    //     $("#nav").toggleClass("see-nav");
    //
    // });

    //Slider
    const intro = $("#intro");

    intro.slick({
        infinite: true,
        speed: 800,
        dots: false,
        autoplay: true,
        arrows: false,
        slidesToShow: 1,
        slidesToScroll: 1,
    });

    $("#intro__arrow--prev").on("click", function (event) {
        event.preventDefault();

        intro.slick('slickPrev');
    });

    $("#intro__arrow--next").on("click", function (event) {
        event.preventDefault();

        intro.slick('slickNext');
    });

    //Select
    $(".select").each(function () {

        var $this = $(this),
            selectOption = $this.find('option'),
            selectOptionLenght = selectOption.length,
            selectedOption = selectOption.filter(':selected'),
            dur = 500;

        $this.hide();

        $this.wrap('<div class="select"></div>');
        $('<div>', {
            class: 'select__gap',
            text: 'Select category...'
        }).insertAfter($this);

        var selectGap = $this.next('.select__gap'),
            caret = selectGap.find('.caret');

        $('<ul>', {
            class: 'select__list'
        }).insertAfter(selectGap);

        var selectList = selectGap.next('.select__list');

        for (var i = 0; i < selectOptionLenght; i++) {
            $('<li>', {
                class: 'select__item',
                html: $('<span>', {
                    text: selectOption.eq(i).text()
                })
            }).attr('data-value', selectOption.eq(i).val()).appendTo(selectList);
        }

        var selectItem = selectList.find('li');

        selectList.slideUp(0);

        selectGap.on('click', function () {

            if (!$(this).hasClass('on')) {
                $(this).addClass('on');
                selectList.slideDown(dur);

                selectItem.on('click', function () {
                    var chooseItem = $(this).data('value');

                    $('select').val(chooseItem).attr('selected', 'selected');
                    selectGap.text($(this).find('span').text());

                    selectList.slideUp(dur);
                    selectGap.removeClass('on');
                });
            } else {
                $(this).removeClass('on');
                selectList.slideUp(dur);
            }

        });

    });

    //Nav
    let nav = $('#post');
    let innerH = nav.innerHeight();
    let scrollOffset = $(window).scrollTop();

    checkScroll(scrollOffset);

    $(window).on("scroll", function () {

        scrollOffset = $(this).scrollTop();
        checkScroll(scrollOffset);

    });

    function checkScroll(scrollOffset) {
        if (scrollOffset >= innerH-300 && $(window).width() > 868) {
            nav.addClass("fixed");
        } else {
            nav.removeClass("fixed");
        }
    }

    function autoType(elementClass, typingSpeed) {
        var thhis = $(elementClass);
        thhis.css({
            "position": "relative",
            "display": "inline-block"
        });
        thhis.prepend('<div class="cursor" style="right: initial; left:0;"></div>');
        thhis = thhis.find(".text-js");
        var text = thhis.text().trim().split('');
        var amntOfChars = text.length;
        var newString = "";
        thhis.text("|");
        setTimeout(function () {
            thhis.css("opacity", 1);
            thhis.prev().removeAttr("style");
            thhis.text("");
            for (var i = 0; i < amntOfChars; i++) {
                (function (i, char) {
                    setTimeout(function () {
                        newString += char;
                        thhis.text(newString);
                    }, i * typingSpeed);
                })(i + 1, text[i]);
            }
        }, 500);
    }

    autoType(".text-js",150);


    new WOW().init();

});
