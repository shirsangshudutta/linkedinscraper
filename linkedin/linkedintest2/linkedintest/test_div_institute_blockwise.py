
from bs4 import BeautifulSoup
import json
import re
html="""
<section id="experience-section" class="pv-profile-section experience-section ember-view"><header class="pv-profile-section__card-header">
  <h2 class="pv-profile-section__card-heading">
    Experience
  </h2>

<!----></header>

  <ul class="pv-profile-section__section-info section-info pv-profile-section__section-info--has-no-more">
<li id="ember2082" class="pv-entity__position-group-pager pv-profile-section__list-item ember-view">        <section id="ember2084" class="pv-profile-section__card-item-v2 pv-profile-section pv-position-entity ember-view">  <div class="display-flex justify-space-between full-width">
<a data-control-name="background_details_company" href="/company/ibm/" id="ember2085" class="full-width ember-view">        <div class="pv-entity__company-details">
  <div class="pv-entity__logo company-logo">
    <img src="https://media-exp1.licdn.com/dms/image/C4E0BAQGfKOtAsJ7gOQ/company-logo_100_100/0?e=1599091200&amp;v=beta&amp;t=luGBb3MHs2C8l7XD2oVMdLydU8-rI-qie4urmsYipEE" loading="lazy" alt="IBM India Private Limited" id="ember2087" class="pv-entity__logo-img EntityPhoto-square-5 lazy-image ember-view">
  </div>
  <div class="pv-entity__company-summary-info">
    <h3 class="t-16 t-black t-bold">
      <span class="visually-hidden">Company Name</span>
      <span>IBM India Private Limited</span>
    </h3>
        <h4 class="t-14 t-black t-normal">
          <span class="visually-hidden">Total Duration</span>
          <span>2 yrs</span>
        </h4>
  </div>
</div>
</a>
<!---->  </div>

    <ul class="pv-entity__position-group mt2">
        <li class="pv-entity__position-group-role-item">
          <div id="ember2089" class="ember-view"><div class="pv-entity__role-details">
  <span class="pv-entity__timeline-node"></span>
  <div class="display-flex justify-space-between full-width">
    <div class="pv-entity__role-container">
      <div class="pv-entity__role-details-container pv-entity__role-details-container--timeline pv-entity__role-details-container--bottom-margin">

        <div class="pv-entity__summary-info-v2 pv-entity__summary-info--background-section pv-entity__summary-info-margin-top ">
          <h3 class="t-14 t-black t-bold">
            <span class="visually-hidden">Title</span>
            <span>Managing Consultant</span>
          </h3>
<!---->            <div class="display-flex">
              <h4 class="pv-entity__date-range t-14 t-black--light t-normal">
                <span class="visually-hidden">Dates Employed</span>
                <span>Jan 2017</span>
              </h4>
                <h4 class="t-14 t-black--light t-normal">
                  <span class="visually-hidden">Employment Duration</span>
                  <span class="pv-entity__bullet-item-v2">less than a year</span>
                </h4>
            </div>

            <h4 class="pv-entity__location t-14 t-black--light t-normal block">
              <span class="visually-hidden">Location</span>
              <span>Kolkata Area, India</span>
            </h4>
<!---->        </div>


<!---->      </div>
    </div>

<!---->  </div>
</div>
</div>
        </li>
        <li class="pv-entity__position-group-role-item">
          <div id="ember2091" class="ember-view"><div class="pv-entity__role-details">
  <span class="pv-entity__timeline-node"></span>
  <div class="display-flex justify-space-between full-width">
    <div class="pv-entity__role-container">
      <div class="pv-entity__role-details-container  ">

        <div class="pv-entity__summary-info-v2 pv-entity__summary-info--background-section pv-entity__summary-info-margin-top ">
          <h3 class="t-14 t-black t-bold">
            <span class="visually-hidden">Title</span>
            <span>Senior System Analyst</span>
          </h3>
<!---->            <div class="display-flex">
              <h4 class="pv-entity__date-range t-14 t-black--light t-normal">
                <span class="visually-hidden">Dates Employed</span>
                <span>Oct 2015 – Dec 2016</span>
              </h4>
                <h4 class="t-14 t-black--light t-normal">
                  <span class="visually-hidden">Employment Duration</span>
                  <span class="pv-entity__bullet-item-v2">1 yr 3 mos</span>
                </h4>
            </div>

            <h4 class="pv-entity__location t-14 t-black--light t-normal block">
              <span class="visually-hidden">Location</span>
              <span>Kolkata Area, India</span>
            </h4>
<!---->        </div>


<!---->      </div>
    </div>

<!---->  </div>
</div>
</div>
        </li>
    </ul>

<!----></section>
</li><li id="ember2093" class="pv-entity__position-group-pager pv-profile-section__list-item ember-view">        <section id="503098743" class="pv-profile-section__card-item-v2 pv-profile-section pv-position-entity ember-view">  <div class="display-flex justify-space-between full-width">
    <div class="display-flex flex-column full-width">
<a data-control-name="background_details_company" href="/search/results/all/?keywords=Wipro" id="ember2096" class="full-width ember-view">          <div class="pv-entity__logo company-logo">
  <img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" loading="lazy" alt="Wipro" id="ember2098" class="pv-entity__logo-img EntityPhoto-square-5 lazy-image ghost-company ember-view">
</div>
<div class="pv-entity__summary-info pv-entity__summary-info--background-section ">
  <h3 class="t-16 t-black t-bold">Architect</h3>
  <p class="visually-hidden">Company Name</p>
  <p class="pv-entity__secondary-title t-14 t-black t-normal">
      Wipro
<!---->  </p>
    <div class="display-flex">
    <h4 class="pv-entity__date-range t-14 t-black--light t-normal">
      <span class="visually-hidden">Dates Employed</span>
      <span>Dec 2013 – Oct 2015</span>
    </h4>
      <h4 class="t-14 t-black--light t-normal">
        <span class="visually-hidden">Employment Duration</span>
        <span class="pv-entity__bullet-item-v2">1 yr 11 mos</span>
      </h4>
  </div>

  <h4 class="pv-entity__location t-14 t-black--light t-normal block">
    <span class="visually-hidden">Location</span>
    <span>Kolkata Area, India</span>
  </h4>

<!---->
</div>

</a>
<!---->    </div>

<!---->  </div>
</section>
</li><li id="ember2101" class="pv-entity__position-group-pager pv-profile-section__list-item ember-view">        <section id="473904771" class="pv-profile-section__card-item-v2 pv-profile-section pv-position-entity ember-view">  <div class="display-flex justify-space-between full-width">
    <div class="display-flex flex-column full-width">
<a data-control-name="background_details_company" href="/company/ibm/" id="ember2104" class="full-width ember-view">          <div class="pv-entity__logo company-logo">
  <img src="https://media-exp1.licdn.com/dms/image/C4E0BAQGfKOtAsJ7gOQ/company-logo_100_100/0?e=1599091200&amp;v=beta&amp;t=luGBb3MHs2C8l7XD2oVMdLydU8-rI-qie4urmsYipEE" loading="lazy" alt="IBM" id="ember2106" class="pv-entity__logo-img EntityPhoto-square-5 lazy-image ember-view">
</div>
<div class="pv-entity__summary-info pv-entity__summary-info--background-section ">
  <h3 class="t-16 t-black t-bold">Senior System Analyst</h3>
  <p class="visually-hidden">Company Name</p>
  <p class="pv-entity__secondary-title t-14 t-black t-normal">
      IBM
<!---->  </p>
    <div class="display-flex">
    <h4 class="pv-entity__date-range t-14 t-black--light t-normal">
      <span class="visually-hidden">Dates Employed</span>
      <span>Feb 2006 – Dec 2013</span>
    </h4>
      <h4 class="t-14 t-black--light t-normal">
        <span class="visually-hidden">Employment Duration</span>
        <span class="pv-entity__bullet-item-v2">7 yrs 11 mos</span>
      </h4>
  </div>

  <h4 class="pv-entity__location t-14 t-black--light t-normal block">
    <span class="visually-hidden">Location</span>
    <span>Kolkata Area, India</span>
  </h4>

<!---->
</div>

</a>
<!---->    </div>

<!---->  </div>
</section>
</li><li id="ember2109" class="pv-entity__position-group-pager pv-profile-section__list-item ember-view">        <section id="159482264" class="pv-profile-section__card-item-v2 pv-profile-section pv-position-entity ember-view">  <div class="display-flex justify-space-between full-width">
    <div class="display-flex flex-column full-width">
<a data-control-name="background_details_company" href="/company/infosys/" id="ember2112" class="full-width ember-view">          <div class="pv-entity__logo company-logo">
  <img src="https://media-exp1.licdn.com/dms/image/C4E0BAQGcC5nkmHu2cg/company-logo_100_100/0?e=1599091200&amp;v=beta&amp;t=rPRqwVCgBeGTI2sOrctd8Vy6bh_Iv3aCrwmNEZfWveA" loading="lazy" alt="Infosys Technologies Ltd" id="ember2114" class="pv-entity__logo-img EntityPhoto-square-5 lazy-image ember-view">
</div>
<div class="pv-entity__summary-info pv-entity__summary-info--background-section ">
  <h3 class="t-16 t-black t-bold">Software Engineer</h3>
  <p class="visually-hidden">Company Name</p>
  <p class="pv-entity__secondary-title t-14 t-black t-normal">
      Infosys Technologies Ltd
<!---->  </p>
    <div class="display-flex">
    <h4 class="pv-entity__date-range t-14 t-black--light t-normal">
      <span class="visually-hidden">Dates Employed</span>
      <span>Sep 2004 – Feb 2006</span>
    </h4>
      <h4 class="t-14 t-black--light t-normal">
        <span class="visually-hidden">Employment Duration</span>
        <span class="pv-entity__bullet-item-v2">1 yr 6 mos</span>
      </h4>
  </div>

<!---->
<!---->
</div>

</a>
<!---->    </div>

<!---->  </div>
</section>
</li>  </ul>

<!----></section>
"""
html_soup = BeautifulSoup(html,'lxml')
name = html_soup.find("li", {"class": "inline t-24 t-black t-normal break-words"})
#print(name.text)

insti = html_soup.find_all("div", {"class": "pv-entity__summary-info pv-entity__summary-info--background-section"})

IDs = []
Defaults = {'id':'','College':'', 'Degree':'','start':''}
thisdict = dict.fromkeys(IDs, Defaults)
i=0
while(i<len(insti)):
  t=insti[i]  
  college=t.find("h3",{"class":"pv-entity__school-name t-16 t-black t-bold"})
  degree=t.find("span",{"class":"pv-entity__comma-item"})
  duration=t.find("p",{"class":"pv-entity__dates t-14 t-black--light t-normal"}).find("span",{"class":""})
  thisdict[i]={'id':i,'college': college.text, 'degree': degree.text,'start':duration.text.strip()}
  i=i+1
# for x, y in thisdict.items():
#   print(x, y)
exp=html_soup.find_all("div", {"class":"pv-entity__summary-info pv-entity__summary-info--background-section mb2"})
#print(exp)
IDs = []
Defaults = {'id':'','designation':'', 'company':'','dates_employed':'','employ_duration':''}
expdict = dict.fromkeys(IDs, Defaults)
#print(len(exp))
j=0
while(j<len(exp)):
  k=exp[j]  
  designation=k.find("h3",{"class":"t-16 t-black t-bold"})
  company=k.find("p",{"class":"pv-entity__secondary-title t-14 t-black t-normal"})
  dates_employed=k.find("h4",{"class":"pv-entity__date-range t-14 t-black--light t-normal"}).find("span",{"class":""})
  #clsprint(dates_employed.text)
  #dates_employed1=dates_employed.find("span",{"class":"visually-hidden"})
  employ_duration=k.find("span",{"class":"pv-entity__bullet-item-v2"})
  #print(employ_duration)
  expdict[j]={'id':i,'designation': designation.text, 'company': company.text.strip(),'dates_employed':dates_employed.text,'employ_duration':employ_duration.text}
  j=j+1
# for x, y in expdict.items():
#   print(x, y)
ids1=[]
Defaults1 = {'Name':'','Edu':'', 'Exp':''}
Recdict = dict.fromkeys(ids1, Defaults1) 
Recdict[0]={'Name':name.text.strip(),'Edu':thisdict, 'Exp':expdict}
# for x, y in Recdict.items():
#   print(x, y) 
# with open('e:\\result.json', 'w') as fp:
#     json.dump(Recdict, fp)
# for p_id, p_info in Recdict.items():
#     print("\nPerson ID:", p_id,p_info)
    # for  key,value in p_info.items():
    #   print(key+':',value)
    