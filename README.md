# Photo Portfolio

[![My Skills](https://skillicons.dev/icons?i=flask,py,html,vercel)](#)

A simple and elegant photo gallery portfolio website built with Flask.



# Why Photo Portfolio?
- [x] **Fast🚀:** 97 performance score on [PSI](https://pagespeed.web.dev/analysis/https-haozheli-pictures/4ccl9diswh?form_factor=mobile) when loading more than 30 pictures. Photos will ready to be viewed within 0.4 seconds. 
- [x] **Easy🎂:** [![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FHaozhe-Li%2Fphoto-portfolio) with one click. Easy to deploy to any serverless platforms. GUI provided for setting or updating website. Coding is slightly required.
- [x] **Responsive🌆:** Responsive design allowed contents to be displayed in varied screen size.



# Usage

#### Quick Start

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

#### Beta features

- **Batch Pictures Upload:** Copy and paste all your pictures you wish to uplaod to `/tests/image_folder`, and run the python script `python3 update_picdb_from_folder.py` under `/tests` directory. All the pictures will be loaded into database with filename as title, and empty description.

# Contribution

Pull request and Issues are welcome! Don't hesitate to question us.



# License

This project is licensed under the [MIT](LICENSE).