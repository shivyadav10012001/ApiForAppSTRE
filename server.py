from flask import Flask,jsonify,request
app=Flask(__name__)

data={
    "success":True,
    "appData":[
        
    {
        "id":"1",
        "app_id":"101",
        "app_name":"Spotify",
        "app_size":"150MB",
        "app_rating":"4.5",
        "publisher":"Spotify Inc",
        "app_downloads":"120M",
        "app_image":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682317961/CustomApp%20Store/spotify_yrwfvv.png",
        "description":"Listen to songs ,play podcasts, create playlists and discover music you'll love",
        "developer_contact":"android-support@spotify.com",
        "imgScreen1":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654910/AppPhotosForCustomAppStore/s1_p7yhfl.webp",
        "imgScreen2":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654908/AppPhotosForCustomAppStore/s2_ojptsh.webp",
        "imgScreen3":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654908/AppPhotosForCustomAppStore/s3_wwfc1g.webp",
        "imgScreen4":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654908/AppPhotosForCustomAppStore/s4_v6dlnh.webp"
        
    },
      {
        "id":"2",
        "app_id":"102",
        "app_name":"Youtube",
        "app_size":"100MB",
        "app_rating":"4.6",
        "publisher":"Alphabet Inc",
        "app_downloads":"900M",
        "app_image":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682317961/CustomApp%20Store/youtube_nfc0my.png",
        "description":"Enjoy your favorite videos and channels with the official Youtube app",
        "developer_contact":"android-support@youtube.com",
        
        "imgScreen1":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654914/AppPhotosForCustomAppStore/y1_bqhmmf.webp",
        "imgScreen2":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654914/AppPhotosForCustomAppStore/y2_laratc.webp",
        "imgScreen3":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654914/AppPhotosForCustomAppStore/y3_te67br.webp",
        "imgScreen4":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654915/AppPhotosForCustomAppStore/y4_d50mwz.webp"
        
        
    },
        {
        "id":"3",
        "app_id":"103",
        "app_name":"Instagram",
        "app_size":"200MB",
        "app_rating":"4.3",
        "publisher":"Meta Inc",
        "app_downloads":"220M",
        "app_image":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682317960/CustomApp%20Store/instagram_dlb3bw.png",
        "description":"Instagram (from Meta) allows you to create and share your photos, stories, reels and videos with the friends and followers you care about. Connect with friends, share what you're up to, or see what's new from others all over the world. Explore our community where you can feel free to be yourself and share everything from your daily moments to life's highlights.",
        "developer_contact":"android-support@meta.com",
        
        "imgScreen1":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654877/AppPhotosForCustomAppStore/i1_p0irao.webp",
        "imgScreen2":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654881/AppPhotosForCustomAppStore/i2_ijomqd.webp",
        "imgScreen3":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654874/AppPhotosForCustomAppStore/i3_prbazv.webp",
        "imgScreen4":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654902/AppPhotosForCustomAppStore/i4_jobuig.webp"
        
        
    },
          {
        "id":"4",
        "app_id":"104",
        "app_name":"Whatsapp",
        "app_size":"350MB",
        "app_rating":"4.6",
        "publisher":"Meta Inc",
        "app_downloads":"110M",
        "app_image":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682317961/CustomApp%20Store/whatsapp_jf0wy2.png",
        "description":"WhatsApp from Meta is a FREE messaging and video calling app. It’s used by over 2B people in more than 180 countries. It’s simple, reliable, and private, so you can easily keep in touch with your friends and family. WhatsApp works across mobile and desktop even on slow connections, with no subscription fees*.",
        "developer_contact":"android-support@meta.com",
        
        "imgScreen1":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682504176/AppPhotosForCustomAppStore/w1_z51yf9.webp",
        "imgScreen2":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682504176/AppPhotosForCustomAppStore/w3_xf80bu.webp",
        "imgScreen3":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682504176/AppPhotosForCustomAppStore/w2_zr4omy.webp",
        "imgScreen4":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654914/AppPhotosForCustomAppStore/w4_bxe3q7.webp"
        
        
    },
            {
        "id":"5",
        "app_id":"105",
        "app_name":"LinkedIn",
        "app_size":"100MB",
        "app_rating":"4.9",
        "publisher":"LinkedIN Inc",
        "app_downloads":"410M",
        "app_image":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682317960/CustomApp%20Store/linkedin_xvtvzw.png",
        "description":"Join LinkedIn, one of the largest professional social apps. Search for jobs, follow the latest business news, and start networking all from one app. Find the right community, workplace and connections to lead you to your ideal career. Start your next job search, browse through salary insights and job listings and connect with business professionals – your next step to your career is here.",
        "developer_contact":"android-support@linkedin.com",
        
        "imgScreen1":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654883/AppPhotosForCustomAppStore/l1_by9t9u.webp",
        "imgScreen2":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654898/AppPhotosForCustomAppStore/l2_umyvfd.webp",
        "imgScreen3":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654885/AppPhotosForCustomAppStore/l3_ftgetw.webp",
        "imgScreen4":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654882/AppPhotosForCustomAppStore/l4_xiceng.webp"
        
        
    },
              {
        "id":"6",
        "app_id":"106",
        "app_name":"Facebook",
        "app_size":"250MB",
        "app_rating":"4.2",
        "publisher":"Meta Inc",
        "app_downloads":"610M",
        "app_image":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682317960/CustomApp%20Store/facebook_bsdpoc.png",
        "description":"Keeping up with friends is faster and easier than ever. Share updates and photos, engage with friends and Pages, and stay connected to communities important to you.",
        "developer_contact":"android-support@meta.com",
        
        "imgScreen1":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654869/AppPhotosForCustomAppStore/fb1_vfdizn.webp",
        "imgScreen2":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654870/AppPhotosForCustomAppStore/fb2_mspw6l.webp",
        "imgScreen3":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654871/AppPhotosForCustomAppStore/fb3_hw3psm.webp",
        "imgScreen4":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654870/AppPhotosForCustomAppStore/fb4_tncukp.webp"
        
        
    },
              
                {
        "id":"7",
        "app_id":"107",
        "app_name":"Medium",
        "app_size":"100MB",
        "app_rating":"4.4",
        "publisher":"Medium Company Inc",
        "app_downloads":"310M",
        "app_image":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682317960/CustomApp%20Store/medium_uwn1jw.png",
        "description":"Medium is the internets encyclopedia of expertise",
        "developer_contact":"android-support@medium.com",
        
        "imgScreen1":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654883/AppPhotosForCustomAppStore/m1_kqtq6l.webp",
        "imgScreen2":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654886/AppPhotosForCustomAppStore/m2_ydua4a.webp",
        "imgScreen3":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654899/AppPhotosForCustomAppStore/m3_iwdgqk.webp",
        "imgScreen4":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654889/AppPhotosForCustomAppStore/m4_jfp5ll.webp"
        
        
    },
                  {
        "id":"8",
        "app_id":"108",
        "app_name":"Twitter",
        "app_size":"300MB",
        "app_rating":"4.3",
        "publisher":"X corp",
        "app_downloads":"780M",
        "app_image":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682317961/CustomApp%20Store/twitter_ifvxzd.png",
        "description":"Expand your social network and stay updated on whats trending now. Retweet, chime in on a thread, go viral, or just scroll through the Twitter timeline to stay on top of whats happening, whether its social media news or news from around the world.",
        "developer_contact":"android-support@twitter.com",
        
        "imgScreen1":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654909/AppPhotosForCustomAppStore/t1_huzekg.webp",
        "imgScreen2":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654910/AppPhotosForCustomAppStore/t2_r2jity.webp",
        "imgScreen3":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654909/AppPhotosForCustomAppStore/t3_eivnpe.webp",
        "imgScreen4":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654910/AppPhotosForCustomAppStore/t4_kicnav.webp"
        
        
    },
                   {
        "id":"9",
        "app_id":"109",
        "app_name":"Tiktok",
        "app_size":"300MB",
        "app_rating":"2.9",
        "publisher":"China Company Inc",
        "app_downloads":"10M",
        "app_image":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682317961/CustomApp%20Store/tiktok_xh72fa.png",
        "description":"A place for Real Talents -TikTok is an entertaining & infortaining short-form video app covering high-quality short videos such as comedy, dance, lipsync, drama, food, lifestyle and fashion.",
        "developer_contact":"android-support@china.com",
        
        "imgScreen1":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654910/AppPhotosForCustomAppStore/tik1_acf9fa.webp",
        "imgScreen2":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654911/AppPhotosForCustomAppStore/tik2_ro5pfy.webp",
        "imgScreen3":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654911/AppPhotosForCustomAppStore/tik3_grntfe.webp",
        "imgScreen4":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654911/AppPhotosForCustomAppStore/tik4_xx0l9x.webp"
        
        
    },
                    {
        "id":"10",
        "app_id":"110",
        "app_name":"Reddit",
        "app_size":"80MB",
        "app_rating":"4.6",
        "publisher":"reddit Inc",
        "app_downloads":"230M",
        "app_image":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682317961/CustomApp%20Store/reddit_k89cra.png",
        "description":"Reddit is the place where people come together to have the most authentic and interesting conversations on the internet—Where gaming communities, nostalgic internet forums, bloggers, meme-makers, and fandoms mingle alongside video streamers, support groups, news junkies, armchair experts, seasoned professionals, and artists and creators of all types.",
        "developer_contact":"android-support@reddit.com",
        
        "imgScreen1":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654900/AppPhotosForCustomAppStore/r1_zapeti.webp",
        "imgScreen2":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654901/AppPhotosForCustomAppStore/r2_aitxr1.webp",
        "imgScreen3":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654902/AppPhotosForCustomAppStore/r3_cf9bxv.webp",
        "imgScreen4":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654902/AppPhotosForCustomAppStore/r4_mvbq5e.webp"
        
        
    },
                     {
        "id":"11",
        "app_id":"111",
        "app_name":"Pintrest",
        "app_size":"120MB",
        "app_rating":"4.1",
        "publisher":"pin Inc",
        "app_downloads":"140M",
        "app_image":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682317960/CustomApp%20Store/pintrest_bosbh5.png",
        "description":"Pinterest is the place to explore inspiration. You can:",
        "developer_contact":"android-support@pin.com",
        
        "imgScreen1":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654893/AppPhotosForCustomAppStore/p1_o8jnsa.webp",
        "imgScreen2":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654898/AppPhotosForCustomAppStore/p2_qwhxfy.webp",
        "imgScreen3":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654898/AppPhotosForCustomAppStore/p3_u13fsr.webp",
        "imgScreen4":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654897/AppPhotosForCustomAppStore/p4_seu5mm.webp"
        
        
    },
                     {
        "id":"12",
        "app_id":"112",
        "app_name":"Messenger",
        "app_size":"350MB",
        "app_rating":"3.5",
        "publisher":"Meta Inc",
        "app_downloads":"780M",
        "app_image":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682317960/CustomApp%20Store/messenger_rqh76u.png",
        "description":"Be together whenever, with our free* all-in-one communication app, complete with unlimited text, voice, video calling and group video chat features..",
        "developer_contact":"android-support@meta.com",
        
        "imgScreen1":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654871/AppPhotosForCustomAppStore/fbm1_gcjbzg.webp",
        "imgScreen2":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654866/AppPhotosForCustomAppStore/bm2_nzaclp.webp",
        "imgScreen3":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654871/AppPhotosForCustomAppStore/fbm3_jtpqrk.webp",
        "imgScreen4":"https://res.cloudinary.com/dp7xhff6v/image/upload/v1682654870/AppPhotosForCustomAppStore/fbm4_glfymy.webp"
        
        
    }
                     ]}
                     

@app.route('/')
def hii():    
    return (jsonify(data))

@app.post('/app')
def p():
    app_id=int(request.args.get("app_id"))
    
    if (app_id >=101 and app_id <=112):
       
        b= (app_id-101)
        d=data["appData"]
        return jsonify( d[b] )
    else:
        return("Enter the valid app_id")

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True, port=8100, ssl_context='adhoc')


    
