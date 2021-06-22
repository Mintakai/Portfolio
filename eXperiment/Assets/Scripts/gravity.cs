using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class gravity : MonoBehaviour
{
    Rigidbody rbPlayerX;
    float gravityForce = 9.81f;
    Vector3 dir;

    // Start is called before the first frame update
    void Start()
    {
        rbPlayerX = GameObject.Find("playerX").GetComponent<Rigidbody>();
    }

    // Update is called once per frame
    void FixedUpdate()
    {
        rbPlayerX.AddForce((gameObject.transform.position - rbPlayerX.transform.position).normalized * gravityForce);
        Debug.Log(rbPlayerX.position);
    }
}
