using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class controlsX : MonoBehaviour
{
    Rigidbody rbPlayerX;
    System.Random rng;

    // Start is called before the first frame update
    void Start()
    {
        rng = new System.Random();
        rbPlayerX = gameObject.GetComponent<Rigidbody>();
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetMouseButtonDown(1))
        {
            rbPlayerX.AddForce(rng.Next(-100, 100), rng.Next(0, 1000), rng.Next(-100, 100));
        }
    }
}
