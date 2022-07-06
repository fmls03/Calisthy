function check_user(){
    if(this.$session.get('username')){
        if(this.$session.get('username') === 'admin'){
            window.location.replace('/admin')
        }
        else{
            window.location.replace('/home')
        }
    }
    else{
        this.$session.clear()
        window.location.replace('/login')
    }
}