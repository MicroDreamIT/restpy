<template>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card">
                    <div class="card-header">Testing Compo</div>
                    <div class="card-body">
                        <form @submit.prevent="post()" class="form-horizontal">
                            <div class="form-group">
                                <label>title</label>
                                <input type="text" v-model="title" class="form-control">
                            </div>
                            <div class="form-group">
                                <label>Description</label>
                                <textarea name="description" class="form-control" v-model="description"></textarea>
                            </div>
                            <div class="form-group">
                                <button class="btn btn-success" type="submit">Submit</button>
                            </div>
                        </form>
                        <ul class="list-group">
                            <li class="list-group-item" v-for="item in items">
                                <p>{{item.id}}. {{item.title}}</p>
                                <p>{{item.description}}</p>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data(){
            return {
                title:'',
                description:'',
                items:[]
            }
        },
        created() {
            console.log('hello')
            axios.get('/api/todo/').then(res=>{
                this.items=res.data
            })
        },
        methods:{
            post(){
                console.log('hello post')

            }
        }
    }
</script>
