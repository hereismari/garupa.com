package controllers;

import models.User;
import play.data.Form;
import play.mvc.Controller;
import play.mvc.Result;
import views.html.index;
import views.html.submit;

import static play.data.Form.form;

public class Application extends Controller {

    static final Form<User> userForm = form(User.class);

    public Result index() {
        return ok(index.render(userForm));
    }

    public Result submit() {
        //Define o formulário
        Form<User> filledForm = userForm.bindFromRequest();
        //Pega o que foi preenchido no formulário
        User created = filledForm.get();
        //Envia o objeto "created" para a View. O objeto "submit" representa a view.
        return ok(submit.render(created));
    }
}
