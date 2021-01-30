//Nav,BurgerMenu
let nav = Vue.createApp({
    data: () => ({
        isActive: false,
        isFixed: false,
        width: 0,
        scrollPosition: 0,
    }),
    methods: {
        toggleMenu() {
            this.isActive = !this.isActive;
            console.log(1);
        },
        updateWidth() {
            this.width = window.innerWidth;
            if (this.width > 768) {
                this.isActive = false;
            }
        },
        onScroll() {
            this.scrollPosition = window.scrollY;
            this.isFixed = this.scrollPosition > 2;
        },
    },
    created() {
        window.addEventListener('resize', this.updateWidth);
        window.addEventListener('scroll', this.onScroll);
    },
    destroyed() {
        window.removeEventListener('resize', this.updateWidth);
    },
});

nav.mount('#app');


//SearchScroll,ShortText
let search = Vue.createApp({
    data: () => ({
        texts: document.querySelectorAll('.posts__text'),
        width: window.innerWidth,
        scrollPosition: 0,
        footerHeight: window.innerHeight,
        info: [],
    }),
    computed: {
        fixedReady() {
            return this.width > 868 && this.scrollPosition > 550;
        },
    },
    methods: {
        updateWidth() {
            this.width = window.innerWidth;
        },
        updateScroll() {
            this.scrollPosition = window.scrollY;
        }
    },
    created() {
        window.addEventListener('resize', this.updateWidth);
        window.addEventListener('scroll', this.updateScroll);
        axios.get('/api/posts/')
            .then(function (response) {
                this.info = response.data;
                console.log(this.info);
            });
    },

});

search.mount('#posts__search-system');

//AutoTypeAnimation
let autoAnimation = Vue.createApp({
    data: () => ({
        speed: 150,
        autoText: '.text-js',
    }),
    mounted() {
        autoType(this.autoText, this.speed);
    },
});
autoAnimation.mount('#log');


//RegistrationForm
let registration = Vue.createApp({
    data: () => ({
        user: {
            username: '',
            email: '',
            password: '',
            rep_password: '',
        },
        patterns: {
            pat_username: /^[а-я]{3,12}|[a-zA-Z0-9_]{3,12}$/,
            pat_email: /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$/,
            pat_password: /^(?=[#$-/:-?{-~!"^_`\[\]a-zA-Z]*([0-9#$-/:-?{-~!"^_`\[\]]))(?=[#$-/:-?{-~!"^_`\[\]a-zA-Z0-9]*[a-zA-Z])[#$-/:-?{-~!"^_`\[\]a-zA-Z0-9]{4,}$/,
        },
    }),
    computed: {
        formReady() {
            return !!(this.valid_username && this.valid_email && this.valid_password && this.valid_rep_password);
        },
        valid_username() {
            console.log(1);
            return this.patterns.pat_username.test(this.user.username);
        },
        valid_email() {
            return this.patterns.pat_email.test(this.user.email);
        },
        valid_password() {
            return this.patterns.pat_password.test(this.user.password);
        },
        valid_rep_password() {
            return this.user.password === this.user.rep_password;
        }
    },
    methods: {
        clickBtn() {
            if (this.formReady) {
                console.log(this.user);
            }
        },
    },
});
registration.mount('#registr');


function autoType(elementClass, typingSpeed) {
    let thhis = $(elementClass);
    thhis.css({
        "position": "relative",
        "display": "inline-block"
    });
    thhis.prepend('<div class="cursor" style="right: initial; left:0;"></div>');
    thhis = thhis.find(".text-js");
    let text = thhis.text().trim().split('');
    let amntOfChars = text.length;
    let newString = "";
    thhis.text("|");
    setTimeout(function () {
        thhis.css("opacity", 1);
        thhis.prev().removeAttr("style");
        thhis.text("");
        for (let i = 0; i < amntOfChars; i++) {
            (function (i, char) {
                setTimeout(function () {
                    newString += char;
                    thhis.text(newString);
                }, i * typingSpeed);
            })(i + 1, text[i]);
        }
    }, 500);
}
