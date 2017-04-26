package com.example.jorgeespina.drive;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageButton;
import android.widget.Button;

public class Registro extends AppCompatActivity {

    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_registro);
        /*ImageButton boton = (ImageButton) findViewById(R.id.Regresar);
        boton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v1) {
                Intent nuevoform = new Intent(Registro.this,Main.class);
                startActivity(nuevoform);
            }
        });

      /*  ImageButton boton1 = (ImageButton) findViewById(R.id.Registro);
        boton1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v1) {
                Intent nuevoform = new Intent(Main.this,Registro.class);
                startActivity(nuevoform);
            }
        });
*/

    }
}
