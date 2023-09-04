package com.example.noralma

import android.annotation.SuppressLint
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.EditText
import android.widget.TextView

class MainActivity : AppCompatActivity() {
    private lateinit var texto:TextView
    @SuppressLint("MissingInflatedId")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        val btn1: Button = findViewById(R.id.btn1)
        texto = findViewById(R.id.txt1)
        
        val eTxt: EditText = findViewById(R.id.eTxt1)
    }
}
