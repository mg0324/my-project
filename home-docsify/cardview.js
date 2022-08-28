(function(){
    Vue.component('ReverseText', {
    props: ['text'],
    template: `
        <div class="reverse-text">
        {{ reversedText }}xxxxx
        <v-style>
        .reverse-text {
            border: 1px solid var(--border-color);
            padding: 20px;
            font-weight: bold;
            border-radius: 4px;
        }
        </v-style>
        </div>
    `,
    computed: {
        reversedText() {
        return this.text.split('').reverse().join('')
        }
    }
    })
})();
