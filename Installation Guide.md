![alt="Sales Analysis"](./Images/sales-analysis.png)

# Sales Analysis
### Sales Analysis Installation Guide

---

1. Download **streamlit**

Streamlit’s open-source app framework is the easiest way for data scientists and machine learning engineers to create beautiful, performant apps in only a few hours! All in pure Python. All for free.

```shell
pip install streamlit
```

---

2. Run the following commands to confirm installation of all NFA packages. Look for version numbers with at least the following versions.  

```shell

conda list streamlit

```
      
      
```text
streamlit                 1.11.1
```


---

## Troubleshooting

If you experience blank plots rendering in your Jupyter Lab preview, try the following steps:

1. First, clear your browser cache.

    - If using Chrome, you can do this by right clicking and choosing `Inspect` from the drop menu.

    ![clear_browser_cache1](./Images/clear_browser_cache1.PNG)

    - Next, hold down click on the browser reload button which will cause another drop down menu to appear.  From this menu select `Empty Cache and Hard Reload`.

      ![clear_browser_cache2](./Images/clear_browser_cache2.PNG)

3. Then clear the Kernel cache:

    - Click the `Kernel` drop down menu inside Jupyter Lab.  From this menu, click `Restart Kernel and Clear Outputs`.

      ![clear_kernel_cache](./Images/clear_kernel_cache.PNG)

4. After these steps are completed, re-run your notebook. 

5. If your browser is Chrome, and you continue to render blank plots after completing the previous 4 steps, try updating Chrome. Instructions for this can be found [here](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DDesktop&hl=en).

If you have issues with Jupyter Lab, you may need to update your Conda environment. Follow the steps below to update the environment.

1. Deactivate your current Conda environment. This is required in order to update the global Conda environment. Be sure to quit any running applications such as Jupyter prior to deactivating the environment.

    ```shell
    conda deactivate
    ```

2. Update Conda.

    ```shell
    conda update conda
    ```
---