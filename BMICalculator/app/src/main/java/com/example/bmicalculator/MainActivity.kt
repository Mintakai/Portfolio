package com.example.bmicalculator

import android.content.Intent
import android.content.SharedPreferences
import android.content.SharedPreferences.Editor
import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.preference.PreferenceManager.getDefaultSharedPreferences
import com.google.android.material.floatingactionbutton.FloatingActionButton
import com.google.gson.Gson
import com.google.gson.reflect.TypeToken
import java.math.RoundingMode
import java.text.DecimalFormat
import kotlin.math.pow


class MainActivity : AppCompatActivity() {

    var counter = 0
    private var heightSaved = 0.0F

    private fun setList(list: ArrayList<String>, sharedPrefs: SharedPreferences){
        val sp: SharedPreferences = sharedPrefs
        val editor: Editor = sp.edit()
        val gson = Gson()
        val json = gson.toJson(list)
        editor.putString("bmilist", json)
        editor.apply()
    }

    private fun getList(sharedPrefs: SharedPreferences):ArrayList<String>{
        val sp: SharedPreferences = sharedPrefs
        val gson = Gson()
        val json = sp.getString("bmilist", null)
        val type = object :TypeToken<ArrayList<String>>(){}.type
        return gson.fromJson(json, type)
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        setSupportActionBar(findViewById(R.id.toolbar))

        val sharedPref = getDefaultSharedPreferences(this)
        if(sharedPref != null) {
            counter = sharedPref.getInt("counter", 0)
            heightSaved = sharedPref.getFloat("height", 0.0F)
        }

        val height = findViewById<EditText>(R.id.heightInput)

        // Viimeisin pituusarvo tallennetaan asetuksesta huolimatta.
        // Asetus vaikuttaa vain arvon näyttämiseen.
        if(sharedPref.getBoolean("save", false)) {
            height.setText("$heightSaved")
        }
        else {
            height.setText("")
        }

        findViewById<Button>(R.id.historyButton).setOnClickListener(View.OnClickListener { view ->
            val intent = Intent(view.context, BMIListHistory::class.java)
            view.context.startActivity(intent)
        })

        findViewById<FloatingActionButton>(R.id.fab).setOnClickListener()
        {
            val weightCalc = findViewById<EditText>(R.id.weightInput).text.toString().toFloatOrNull()
            val heightCalc = height.text.toString().toFloatOrNull()

            with(sharedPref.edit()) {
                putInt("counter", counter)
                apply()
            }

            if (weightCalc != null && height != null) {
                val sp: SharedPreferences = sharedPref
                val editor: Editor = sp.edit()
                val df = DecimalFormat("#.##")
                df.roundingMode = RoundingMode.CEILING
                val result = df.format((weightCalc / (heightCalc?.pow(2)!!))).toString()
                findViewById<TextView>(R.id.result).text = ("YOUR BMI IS: $result")
                with(editor) {
                    if(sp.contains("bmilist")) {
                        val bmiList = getList(sharedPref)
                        bmiList.add(result)
                        setList(bmiList, sharedPref)
                    } else {
                        setList(arrayListOf(result), sharedPref)
                    }
                    putFloat("height", heightCalc)
                    apply()
                }
            }
            else {
                counter++
                findViewById<TextView>(R.id.result).text = ("Please enter a valid value for weight and height!\nFailures: $counter")
            }
        }
    }

    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        // Inflate the menu; this adds items to the action bar if it is present.
        menuInflater.inflate(R.menu.menu_main, menu)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        return when (item.itemId) {
            R.id.action_settings -> {
                // Avaa settingsActivity
                val intent = Intent(this, SettingsActivity::class.java)

                startActivity(intent)
                true
            }
            else -> super.onOptionsItemSelected(item)
        }
    }
}