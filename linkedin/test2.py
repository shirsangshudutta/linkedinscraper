from bs4 import BeautifulSoup

html1="""<ul class="pv-profile-section__section-info section-info pv-profile-section__section-info--has-no-more">
      <li id="198690695" class="pv-profile-section__list-item pv-education-entity pv-profile-section__card-item ember-view"><div class="display-flex justify-space-between full-width">
  <div class="display-flex flex-column full-width">
<a data-control-name="background_details_school" href="/school/13513/?legacySchoolId=13513" id="ember188" class="ember-view">        <div class="pv-entity__logo">
  <img src="https://media-exp1.licdn.com/dms/image/C510BAQFkGVsBobrK1A/company-logo_100_100/0?e=1598486400&amp;v=beta&amp;t=fpXyKY6NKmkb-7d4BL6-1OwznaPV4VZvb7SN66eF61s" loading="lazy" alt="Jadavpur University" id="ember190" class="pv-entity__logo-img pv-entity__logo-img EntityPhoto-square-4 lazy-image ember-view">
</div>

<div class="pv-entity__summary-info pv-entity__summary-info--background-section">
  <div class="pv-entity__degree-info">
    <h3 class="pv-entity__school-name t-16 t-black t-bold">Jadavpur University</h3>

      <p class="pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal">
        <span class="visually-hidden">Degree Name</span>
        <span class="pv-entity__comma-item">Doctor of Philosophy (PhD)</span>
      </p>
      <p class="pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal">
        <span class="visually-hidden">Field Of Study</span>
        <span class="pv-entity__comma-item">Engineering</span>
      </p>
<!---->  </div>

    <p class="pv-entity__dates t-14 t-black--light t-normal">
      <span class="visually-hidden">Dates attended or expected graduation</span>
      <span>
            <time>2009</time> – <time>2013</time>
      </span>
    </p>

<!----></div>

</a>
<!---->  </div>

<!----></div>
</li>
      <li id="140326635" class="pv-profile-section__list-item pv-education-entity pv-profile-section__card-item ember-view"><div class="display-flex justify-space-between full-width">
  <div class="display-flex flex-column full-width">
<a data-control-name="background_details_school" href="/school/13513/?legacySchoolId=13513" id="ember193" class="ember-view">        <div class="pv-entity__logo">
  <img src="https://media-exp1.licdn.com/dms/image/C510BAQFkGVsBobrK1A/company-logo_100_100/0?e=1598486400&amp;v=beta&amp;t=fpXyKY6NKmkb-7d4BL6-1OwznaPV4VZvb7SN66eF61s" loading="lazy" alt="Jadavpur University" id="ember195" class="pv-entity__logo-img pv-entity__logo-img EntityPhoto-square-4 lazy-image ember-view">
</div>

<div class="pv-entity__summary-info pv-entity__summary-info--background-section">
  <div class="pv-entity__degree-info">
    <h3 class="pv-entity__school-name t-16 t-black t-bold">Jadavpur University</h3>

      <p class="pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal">
        <span class="visually-hidden">Degree Name</span>
        <span class="pv-entity__comma-item">Master's degree</span>
      </p>
      <p class="pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal">
        <span class="visually-hidden">Field Of Study</span>
        <span class="pv-entity__comma-item">Computer Science and Engineering</span>
      </p>
<!---->  </div>

    <p class="pv-entity__dates t-14 t-black--light t-normal">
      <span class="visually-hidden">Dates attended or expected graduation</span>
      <span>
            <time>2003</time> – <time>2005</time>
      </span>
    </p>

<!----></div>

</a>
<!---->  </div>

<!----></div>
</li>
      <li id="140339745" class="pv-profile-section__list-item pv-education-entity pv-profile-section__card-item ember-view"><div class="display-flex justify-space-between full-width">
  <div class="display-flex flex-column full-width">
<a data-control-name="background_details_school" href="/search/results/all/?keywords=Institute%20of%20Engineering%20and%20Management%20(IEM)" id="ember198" class="ember-view">        <div class="pv-entity__logo">
  <img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" loading="lazy" alt="Institute of Engineering and Management (IEM)" id="ember200" class="pv-entity__logo-img pv-entity__logo-img EntityPhoto-square-4 lazy-image ghost-school ember-view">
</div>

<div class="pv-entity__summary-info pv-entity__summary-info--background-section">
  <div class="pv-entity__degree-info">
    <h3 class="pv-entity__school-name t-16 t-black t-bold">Institute of Engineering and Management (IEM)</h3>

      <p class="pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal">
        <span class="visually-hidden">Degree Name</span>
        <span class="pv-entity__comma-item">Bachelor of Technology (B.Tech.)</span>
      </p>
      <p class="pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal">
        <span class="visually-hidden">Field Of Study</span>
        <span class="pv-entity__comma-item">Computer Science</span>
      </p>
<!---->  </div>

    <p class="pv-entity__dates t-14 t-black--light t-normal">
      <span class="visually-hidden">Dates attended or expected graduation</span>
      <span>
            <time>1999</time> – <time>2003</time>
      </span>
    </p>

<!----></div>

</a>
<!---->  </div>

<!----></div>
</li>
  </ul>"""
html_soup=BeautifulSoup(html1,features="html.parser")  
i=0
IDs =[]
Defaults = {'id':'','College':'', 'Degree':'','start':''}
thisdict = dict.fromkeys(IDs, Defaults)
insti= html_soup.find_all("div", {"class": "pv-entity__summary-info pv-entity__summary-info--background-section"})
while(i<len(insti)):
        t=insti[i]  
        college=t.find("h3",{"class":"pv-entity__school-name t-16 t-black t-bold"})
        degree=t.find("span",{"class":"pv-entity__comma-item"})
        duration=t.find("p",{"class":"pv-entity__dates t-14 t-black--light t-normal"})
        thisdict[i]={'id':i,'college': college.text, 'degree': degree.text,'start':duration.text.strip()}
        i=i+1    
for x, y in thisdict.items():
    print(x, y)    
