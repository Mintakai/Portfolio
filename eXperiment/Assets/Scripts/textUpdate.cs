using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class textUpdate : MonoBehaviour
{
    GameObject player;
    Rigidbody rbPlayer;

    public TMP_Text velocityDisplay;
    // Start is called before the first frame update
    void Start()
    {
        player = GameObject.Find("player");
        rbPlayer = player.GetComponent<Rigidbody>();
    }

    // Update is called once per frame
    void Update()
    {
        double roundedVelocity = Mathf.Abs(rbPlayer.velocity.y);
        string rounded = string.Format("{0:0.00}", roundedVelocity);
        velocityDisplay.text = $"velocity: {rounded}";
    }
}
