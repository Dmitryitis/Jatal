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
    $("#burger").on("click", function (event) {
        event.preventDefault();

        $("#nav").toggleClass("see-nav");

    });

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
          