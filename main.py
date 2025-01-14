from email.message import EmailMessage
from email.mime.text import MIMEText
import ssl
import pandas as pd
import smtplib

df = pd.read_csv('UK_charities.csv') 
names = df.iloc[:,2]
emails = df.iloc[:,8]

email_sender = 'ali.elsayed@donnate.org'
email_password = 'galp orav wnep gofc'
subject ='Join Donnate: Amplify Your Impact with Charity Shopping!'
context = ssl.create_default_context()


email_receiver = 'ali-hisham@hotmail.com'
email_receiver_name = 'ali'
email_body = f"""
  <html>
    <body>
      Dear {email_receiver_name},
      <br />
      We hope this message finds you well. We are thrilled to introduce you to
      <a href="https://donnate.org/">Donnate</a>, a revolutionary charity shopping
      platform designed to connect generous sellers with impactful charities like
      yours. At Donnate, we believe in turning everyday transactions into
      meaningful contributions, and we would love for you to join us on this
      journey.
      <br />
      <h3>What is Donnate?</h3>
      <p>
        Donnate is a unique online platform where users can sell their items and
        donate a portion of their proceeds to registered charities. Our mission is
        to create a seamless and engaging way for people to support the causes
        they care about, while also promoting sustainability and community
        involvement.
      </p>
  
      <br />
  
      <h3>Why Partner with Donnate?</h3>
      <ul>
        <li>
          Increase Donations: Gain access to a new stream of donations from
          individuals selling items on our platform.
        </li>
        <li>
          Raise Awareness: Boost your charity’s visibility among a community of
          socially conscious users.
        </li>
        <li>
          Transparency and Trust: Our platform ensures transparent tracking of
          donations, providing both donors and charities with peace of mind.
        </li>
        <li>
          Community Engagement: Engage with a network of supporters who are
          passionate about making a difference.
        </li>
      </ul>
      <h3>How Does It Work?</h3>
      <ul>
        <li>
          Sign Up: Register your charity on our platform. It’s quick, easy, and
          free.
        </li>
  
        <li>
          Get Featured: Create a compelling profile that highlights your mission,
          success stories, and impact.
        </li>
  
        <li>
          Receive Donations: Start receiving donations from users who choose to
          support your cause through their sales.
        </li>
      </ul>
      <p>
        Ready to Amplify Your Impact?
        <br />
        We would be delighted to have you as one of our partner charities. To get
        started, simply click the link below to sign up and create your profile:
      </p>
      <a href="Charity.donnate.org/auth/register"
        >Charity.donnate.org/auth/register</a
      >
      <br />
      If you have any questions, feel free to contact us or learn more about us by
      visiting our website <a href="https://donnate.org/">here</a>. We're here to
      support you every step of the way Thank you for your time and consideration.
      Together, we can turn everyday actions into extraordinary outcomes. <br />
      <br />
      Warm regards,
      <br />
      <br />
      Ali Elsayed
      <br />
      Global Outreach Coordinator
      <br />
      <a href="mailto:ali.elsayed@donnate.org">ali.elsayed@donnate.org</a>
      <br />
      donnate.org
      <br />
      <img src="../image.png" alt="" />
      <div style="display: flex; gap: 10px">
        <img src="../store1.png" alt="" />
        <img src="../store2.png" alt="" />
      </div>
    </body>
  </html>
"""

em = MIMEText(email_body, 'html')
em['From'] = email_sender
em['Subject'] = subject
em['To'] = email_receiver



def send(x, y):
  print(x + ' ' + y)
  # with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
  #   smtp.login(email_sender,email_password)
  #   smtp.sendmail(email_sender, email_receiver, em.as_string())

i=0
for name, mail in zip(names, emails):
  i+=1
  if not mail.startswith('null'):
    send(name, mail)
    time.sleep(3)
  if i > 10:
    break



