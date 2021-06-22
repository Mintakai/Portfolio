using System;
using System.Collections;
using UnityEngine;

public class controls : MonoBehaviour
{
    Rigidbody rbPlayer;
    bool stationary = false;

    // Start is called before the first frame update
    void Start()
    {
        rbPlayer = gameObject.GetComponent<Rigidbody>();
    }

    private void PropelPlayer()
    {
        rbPlayer.AddForce(0, 250, 0);
    }

    private void PropelPlayerRandom()
    {
        System.Random rng = new System.Random();
        rbPlayer.AddForce(rng.Next(-100, 100), 0, rng.Next(-100, 100));
    }

    private void Update()
    {
        if(rbPlayer.velocity.y != 0)
        {
            stationary = false;
        }
        else
        {
            stationary = true;
        }

        if (Input.GetMouseButtonDown(0) && stationary)
        {
            PropelPlayer();
        }
        else if (Input.GetMouseButtonDown(0))
        {
            PropelPlayerRandom();
        }
    }
}
