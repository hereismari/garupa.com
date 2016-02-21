package models;

import com.avaje.ebean.Model;
import javax.persistence.Entity;
import javax.persistence.Id;

@Entity
public class User extends Model {

    private static final long serialVersionUID = 1L;

    @Id
    public Long id;

    public String email;

    public String password;

    public String mobileOS;

    public char gender;

    public User(Long id, String email) {
        this.id = id;
        this.email = email;
        this.password = password;
        this.mobileOS = mobileOS;
        this.gender = gender;
    }
}
