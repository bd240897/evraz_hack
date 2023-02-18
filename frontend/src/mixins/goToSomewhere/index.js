export default {
    data() {
        return {}
    },
    created() {

    },
    methods: {
        goToFirst(id) {
            this.$router.push({name: 'First'})
        },

        goToSecond(id) {
            this.$router.push({name: 'Second', params: { id: id }})
        },

        // goToLogin() {
        //     this.$router.push({name: 'LoginView'})
        // },
        // goToRegister() {
        //     this.$router.push({name: 'RegisterView'})
        // },
        // goToMain() {
        //     this.$router.push({name: 'MainView'})
        // },
        // goToProfile(id) {
        //     console.log(id)
        //     // перейти на страницу экспертов
        //     this.$router.push({name: 'ProfileView'})
        // },
        // goToQuickStart() {
        //     this.$router.push({name: 'QuickStartView'})
        // },
        // goToDoctors() {
        //     this.$router.push({name: 'DoctorsView'})
        // },
    }
}