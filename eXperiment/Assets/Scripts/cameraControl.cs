using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class cameraControl : MonoBehaviour
{
    public Camera firstCamera;
    public Camera secondCamera;

    // Start is called before the first frame update
    void Start()
    {
        firstCamera.enabled = true;
        secondCamera.enabled = false;
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            if (firstCamera.enabled)
            {
                firstCamera.enabled = false;
                secondCamera.enabled = true;
            }
            else
            {
                firstCamera.enabled = true;
                secondCamera.enabled = false;
            }
        }
    }
}
