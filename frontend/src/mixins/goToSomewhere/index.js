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
    }
}