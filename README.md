# Photo Portfolio

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FHaozhe-Li%2Fphoto-portfolio)

A simple and elegant photo gallery / portfolio website built with Flask.



# Usage

1. Clone the repository

   ````
   https://github.com/Haozhe-Li/photo-portfolio.git
   ````

2. Install the dependencies:

   ````bash
   pip install -r requirements.txt
   ````

3. Go to your project directory and change to the **``client``** folder using a command like ``cd client``: 

   - Use ``python3 config_handler.py`` to configure the site name, site title, etc.
   - Use ``python3 upload_handler.py`` to upload image and add description and title for it.

4. For those time when you want to update your gallery, repeat **Step 3** to reconfigure or upload new images. Deleting images is **NOT** available yet.

5. Go back to your project directory, then build your website with the following command

   ````bash
   python3 app.py
   ````

   Then you should be able to visit ``http://127.0.0.1:5000`` to preview your website.



# License

This project is licensed under the [MIT](LICENSE).