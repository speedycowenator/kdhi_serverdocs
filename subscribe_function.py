'''
<a id="save_button" class="{{subscription_status}}" onclick="add_cart()"></a>
<script>
function add_cart() {
    if (document.getElementById("save_button").className == "object_not_in_saved_list") {
        var xhttp;
        direction       = "ADD"
        object_model    = "{{content_object.parentname}}"
        object_pk       = "{{content_object.pk}}"
        csrfmiddlewaretoken = "{{ csrf_token }}"
        xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
              document.getElementById("save_button").className = this.responseText;
            }
        };
        xhttp.open("POST", "{% url 'shopping_cart_update' %}");
        xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhttp.send("direction=" + direction + "&object_model=" + object_model + "&object_pk=" + object_pk + "&csrfmiddlewaretoken=" + csrfmiddlewaretoken);
    }
    if (document.getElementById("save_button").className == "object_in_saved_list") {
        var xhttp;
        direction       = "SUB"
        object_model    = "{{content_object.parentname}}"
        object_pk       = "{{content_object.pk}}"
        csrfmiddlewaretoken = "{{ csrf_token }}"
        xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
              document.getElementById("save_button").className = this.responseText;

            }
        };
        xhttp.open("POST", "{% url 'shopping_cart_update' %}");
        xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhttp.send("direction=" + direction + "&object_model=" + object_model + "&object_pk=" + object_pk + "&csrfmiddlewaretoken=" + csrfmiddlewaretoken);
    }
}
</script>
'''