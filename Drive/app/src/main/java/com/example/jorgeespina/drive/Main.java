package com.example.jorgeespina.drive;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.Toast;

public class Main extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        ImageButton boton = (ImageButton) findViewById(R.id.Login);
        boton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v1) {
                Intent nuevoform = new Intent(Main.this,Principal.class);
                startActivity(nuevoform);
            }
        });

        ImageButton boton1 = (ImageButton) findViewById(R.id.Registro);
        boton1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v1) {
                Intent nuevoform = new Intent(Main.this,Registro.class);
                startActivity(nuevoform);
            }
        });


    }
}
