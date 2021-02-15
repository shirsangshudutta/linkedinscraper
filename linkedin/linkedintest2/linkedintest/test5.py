from bs4 import BeautifulSoup
import json
import re
html="""
<section id="education-section" class="pv-profile-section education-section ember-view"><header class="pv-profile-section__card-header">
  <h2 class="pv-profile-section__card-heading">
    Education
  </h2>

<!----></header>

  <ul class="pv-profile-section__section-info section-info pv-profile-section__section-info--has-no-more">
      <li id="438852718" class="pv-profile-section__list-item pv-education-entity pv-profile-section__card-item ember-view"><div class="display-flex justify-space-between full-width">
  <div class="display-flex flex-column full-width">
<a data-control-name="background_details_school" href="/school/13513/?legacySchoolId=13513" id="ember228" class="ember-view">        <div class="pv-entity__logo">
  <img src="https://media-exp1.licdn.com/dms/image/C510BAQFkGVsBobrK1A/company-logo_100_100/0?e=1600905600&amp;v=beta&amp;t=mNx8Ri2ySu4bJXh-Dy03m-GIxKaZ62t53QoMWYqHYdw" loading="lazy" alt="Jadavpur University" id="ember230" class="pv-entity__logo-img pv-entity__logo-img EntityPhoto-square-4 lazy-image ember-view">
</div>

<div class="pv-entity__summary-info pv-entity__summary-info--background-section">
  <div class="pv-entity__degree-info">
    <h3 class="pv-entity__school-name t-16 t-black t-bold">Jadavpur University</h3>

      <p class="pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal">
        <span class="visually-hidden">Degree Name</span>
        <span class="pv-entity__comma-item">Master of Engineering - MEng</span>
      </p>
      <p class="pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal">
        <span class="visually-hidden">Field Of Study</span>
        <span class="pv-entity__comma-item">Information Technology</span>
      </p>
      <p class="pv-entity__secondary-title pv-entity__grade t-14 t-black t-normal">
        <span class="visually-hidden">Grade</span>
        <span class="pv-entity__comma-item">1st Class</span>
      </p>
  </div>

    <p class="pv-entity__dates t-14 t-black--light t-normal">
      <span class="visually-hidden">Dates attended or expected graduation</span>
      <span>
            <time>2014</time> – <time>2017</time>
      </span>
    </p>

<!----></div>

</a>
<!---->  </div>

<!----></div>
</li>
      <li id="47189137" class="pv-profile-section__list-item pv-education-entity pv-profile-section__card-item ember-view"><div class="display-flex justify-space-between full-width">
  <div class="display-flex flex-column full-width">
<a data-control-name="background_details_school" href="/school/20302/?legacySchoolId=20302" id="ember233" class="ember-view">        <div class="pv-entity__logo">
  <img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" loading="lazy" alt="University of Calcutta" id="ember235" class="pv-entity__logo-img pv-entity__logo-img EntityPhoto-square-4 lazy-image ghost-school ember-view">
</div>

<div class="pv-entity__summary-info pv-entity__summary-info--background-section">
  <div class="pv-entity__degree-info">
    <h3 class="pv-entity__school-name t-16 t-black t-bold">University of Calcutta</h3>

      <p class="pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal">
        <span class="visually-hidden">Degree Name</span>
        <span class="pv-entity__comma-item">B.Tech</span>
      </p>
      <p class="pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal">
        <span class="visually-hidden">Field Of Study</span>
        <span class="pv-entity__comma-item">Information Technology</span>
      </p>
      <p class="pv-entity__secondary-title pv-entity__grade t-14 t-black t-normal">
        <span class="visually-hidden">Grade</span>
        <span class="pv-entity__comma-item">1st Class</span>
      </p>
  </div>

    <p class="pv-entity__dates t-14 t-black--light t-normal">
      <span class="visually-hidden">Dates attended or expected graduation</span>
      <span>
            <time>2000</time> – <time>2003</time>
      </span>
    </p>

<!----></div>

</a>
      <div id="ember236" class="pv-entity__extra-details t-14 t-black--light ember-view"><p class="pv-entity__description t-14 t-normal mt4">
  Had special interest in wireless physical layer and Digital Signal Processing. Final year project was done on mobile computing based on Direct Sequence Spread Spectrum.
</p>

<!----></div>
  </div>

<!----></div>
</li>
      <li id="408487523" class="pv-profile-section__list-item pv-education-entity pv-profile-section__card-item ember-view"><div class="display-flex justify-space-between full-width">
  <div class="display-flex flex-column full-width">
<a data-control-name="background_details_school" href="/school/20302/?legacySchoolId=20302" id="ember239" class="ember-view">        <div class="pv-entity__logo">
  <img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" loading="lazy" alt="University of Calcutta" id="ember241" class="pv-entity__logo-img pv-entity__logo-img EntityPhoto-square-4 lazy-image ghost-school ember-view">
</div>

<div class="pv-entity__summary-info pv-entity__summary-info--background-section">
  <div class="pv-entity__degree-info">
    <h3 class="pv-entity__school-name t-16 t-black t-bold">University of Calcutta</h3>

      <p class="pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal">
        <span class="visually-hidden">Degree Name</span>
        <span class="pv-entity__comma-item">Bachelor of Science</span>
      </p>
      <p class="pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal">
        <span class="visually-hidden">Field Of Study</span>
        <span class="pv-entity__comma-item">Electronics (Hons.)</span>
      </p>
      <p class="pv-entity__secondary-title pv-entity__grade t-14 t-black t-normal">
        <span class="visually-hidden">Grade</span>
        <span class="pv-entity__comma-item">1st Class - 3rd</span>
      </p>
  </div>

    <p class="pv-entity__dates t-14 t-black--light t-normal">
      <span class="visually-hidden">Dates attended or expected graduation</span>
      <span>
            <time>1997</time> – <time>2000</time>
      </span>
    </p>

<!----></div>

</a>
<!---->  </div>

<!----></div>
</li>
  </ul>
<!----></section>
"""
#  t=BeautifulSoup(html,'html.parser').find("p",{"class":"pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal"}).find("span",{"class":"pv-entity__comma-item"})
def clean_string(var):
    var=str(var)
    var=var.strip()
    var=var.replace('\n','')
    return var
IDs =[]
Defaults = {'College':'','Degree':'','Branch':'','duration':''}
thisdict = dict.fromkeys(IDs, Defaults)
edusect=BeautifulSoup(html,'html.parser').find("section", {"id":"education-section"})
# print(edusect)
i=0
for t in edusect.find_all("li", {"class": "pv-profile-section__list-item pv-education-entity pv-profile-section__card-item ember-view"}):
                degree=t.find("p",{"class":"pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal"}).find("span",{"class":"pv-entity__comma-item"}).text
                print(degree)
                # colleg1=t.find("h3",{"class":"pv-entity__school-name t-16 t-black t-bold"}).find(text=re.compile("jadavpur university",re.IGNORECASE))
                # print('@@@@@@@@@@2'+colleg1)
                if(t.find("h3",{"class":"pv-entity__school-name t-16 t-black t-bold"}).find(text=re.compile("jadavpur university",re.IGNORECASE))) :
                  thisdict[i]={
                        'college':clean_string(t.find("h3",{"class":"pv-entity__school-name t-16 t-black t-bold"}).text) if t.find("h3",{"class":"pv-entity__school-name t-16 t-black t-bold"}) else '',
                        'degree':t.find("p",{"class":"pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal"}).find("span",{"class":"pv-entity__comma-item"}).text if t.find("p",{"class":"pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal"}) else '',
                        #  if t.find("p",{"class":"pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal"}).find("span",{"class":"pv-entity__comma-item"}) else ''
                        'branch': clean_string(t.find("p",{"class":"pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal"}).find("span",{"class":"pv-entity__comma-item"}).text),
                        'duration':clean_string(t.find("p",{"class":"pv-entity__dates t-14 t-black--light t-normal"}).find("span",{"class":""}).text) if t.find("p",{"class":"pv-entity__dates t-14 t-black--light t-normal"}).find("span",{"class":""}) else ''
                  } 
                i=i+1

# for x, y in thisdict.items():
#         print(x, y)
print(json.dumps(thisdict))
	